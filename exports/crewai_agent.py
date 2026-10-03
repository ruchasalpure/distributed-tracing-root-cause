from crewai import Agent

distributed_tracing_root_cause = Agent(
    role="Distributed Tracing Root Cause",
    goal="Deliver high-precision autonomous Distributed Tracing Root Cause operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
