# System overview

```mermaid
flowchart TD
 U[User] --> G[Gateway]
 G --> M[Master]
 M --> D[Task DAG]
 D --> W[Workspace runner]
 W --> C[Coder]
 W --> T[Tester]
 W --> R[Reviewer]
 R --> E[Evidence and Git diff]
 E --> A[Human approval]
 M --> N[Compute node]
```

The Master owns intent interpretation and delegation. Coder changes only its assigned workspace. Tester and Reviewer are independent roles. Compute absence queues or pauses inference work; it never deletes task state.
