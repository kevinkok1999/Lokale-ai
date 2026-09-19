# Lokale AI Platform

Status: **PRE-CODING FROZEN**

This repository is the canonical implementation repository for the two-node local AI platform.

## Goal

A user-controlled, local-first AI operating platform with:

- AI-Core control plane
- RTX compute node
- dynamic specialist teams
- parallel-by-default orchestration
- durable jobs and recovery
- one-runner GitHub build queue
- zero-config installation goal
- image, video and documentary production
- security, verification, rollback and auditability

## Authority model

The user is the final authority for goals and irreversible decisions.
The assistant/orchestrator executes permitted work, coordinates specialist teams, and must never report unverified work as complete.

## Coding rule

Production implementation starts only after all three pre-coding gates are PASS:

1. Architecture and data contracts
2. Resource, security and installer contracts
3. Engineering, runner, test and release contract

See the documents in `docs/`.
