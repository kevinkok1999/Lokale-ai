# ADR 0001: Separate control and compute

Status: Accepted for freeze candidate.

Context: the 16 GB always-on machine cannot safely host every heavy workload. Decision: durable orchestration/state stays on CONTROL and inference/heavy jobs on authenticated COMPUTE. Trade-off: pairing and queueing add complexity. A FULL role may co-locate services only when doctor validates budgets.
