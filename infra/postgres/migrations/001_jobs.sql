BEGIN;

CREATE SCHEMA IF NOT EXISTS ai_control;

CREATE TABLE IF NOT EXISTS ai_control.schema_version (
    version integer PRIMARY KEY,
    description text NOT NULL,
    applied_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS ai_control.projects (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    slug text NOT NULL UNIQUE,
    name text NOT NULL,
    repository_url text,
    default_branch text NOT NULL DEFAULT 'main',
    status text NOT NULL DEFAULT 'active'
      CHECK (status IN ('active','paused','archived')),
    metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
    created_at timestamptz NOT NULL DEFAULT now(),
    updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS ai_control.nodes (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    node_key text NOT NULL UNIQUE,
    role text NOT NULL CHECK (role IN ('control','compute','runner')),
    hostname text NOT NULL,
    ip_address inet,
    status text NOT NULL DEFAULT 'offline'
      CHECK (status IN ('online','offline','degraded','draining')),
    capabilities jsonb NOT NULL DEFAULT '{}'::jsonb,
    last_heartbeat_at timestamptz,
    metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
    created_at timestamptz NOT NULL DEFAULT now(),
    updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS ai_control.jobs (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id uuid REFERENCES ai_control.projects(id) ON DELETE CASCADE,
    parent_job_id uuid REFERENCES ai_control.jobs(id) ON DELETE SET NULL,
    idempotency_key text,
    job_type text NOT NULL,
    status text NOT NULL DEFAULT 'queued'
      CHECK (status IN (
        'queued','blocked','leased','running','testing','reviewing',
        'waiting_approval','retry_wait','completed','failed','cancelled'
      )),
    priority smallint NOT NULL DEFAULT 3 CHECK (priority BETWEEN 1 AND 5),
    requested_by text NOT NULL DEFAULT 'user',
    target_node_id uuid REFERENCES ai_control.nodes(id) ON DELETE SET NULL,
    required_capabilities jsonb NOT NULL DEFAULT '{}'::jsonb,
    payload jsonb NOT NULL DEFAULT '{}'::jsonb,
    result jsonb,
    max_attempts smallint NOT NULL DEFAULT 3 CHECK (max_attempts BETWEEN 1 AND 10),
    attempt_count smallint NOT NULL DEFAULT 0 CHECK (attempt_count >= 0),
    cancellation_requested boolean NOT NULL DEFAULT false,
    lease_owner text,
    lease_expires_at timestamptz,
    available_at timestamptz NOT NULL DEFAULT now(),
    started_at timestamptz,
    finished_at timestamptz,
    error_code text,
    error_text text,
    created_at timestamptz NOT NULL DEFAULT now(),
    updated_at timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT jobs_idempotency_per_project UNIQUE(project_id, idempotency_key)
);

CREATE UNIQUE INDEX IF NOT EXISTS jobs_global_idempotency_idx
ON ai_control.jobs(idempotency_key)
WHERE project_id IS NULL AND idempotency_key IS NOT NULL;

CREATE TABLE IF NOT EXISTS ai_control.job_dependencies (
    job_id uuid NOT NULL REFERENCES ai_control.jobs(id) ON DELETE CASCADE,
    depends_on_job_id uuid NOT NULL REFERENCES ai_control.jobs(id) ON DELETE CASCADE,
    created_at timestamptz NOT NULL DEFAULT now(),
    PRIMARY KEY (job_id, depends_on_job_id),
    CHECK (job_id <> depends_on_job_id)
);

CREATE INDEX IF NOT EXISTS jobs_status_priority_available_idx
ON ai_control.jobs(status, priority, available_at, created_at);

CREATE INDEX IF NOT EXISTS jobs_lease_expiry_idx
ON ai_control.jobs(lease_expires_at)
WHERE lease_expires_at IS NOT NULL;

INSERT INTO ai_control.schema_version(version, description)
VALUES (1, 'Core durable job state')
ON CONFLICT (version) DO NOTHING;

COMMIT;
