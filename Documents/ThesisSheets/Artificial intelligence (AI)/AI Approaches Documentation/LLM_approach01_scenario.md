# Applying AI Approaches to Predictive Scaling Scenario (Test Scenario 1)

This document details how the different AI approaches (Fine-tuned LLM, RAG, Single Agent, Multi-Agent) could implement the "LLM-Driven Predictive Scaling" test scenario (`LLM_test01_scenario.md`).

**Scenario Recap:** Predict an upcoming traffic surge for a web application and proactively scale Kubernetes resources before the surge hits, maintain performance, and scale down afterward.

## 1. Fine-Tuned LLM Approach

*   **Setup:** A foundational LLM is fine-tuned on historical monitoring data (request rates, CPU/Mem usage, replica counts, event flags like "marketing campaign") from the target web application and potentially similar apps.
*   **Trigger Prediction:** The system feeds current metrics *and* the specific event flag (e.g., `{"event": "upcoming_promo_start_in_15m"}`) into the fine-tuned LLM via the `prediction-api.md`.
*   **Observe Proactive Scaling:**
    *   The fine-tuned LLM, having learned patterns from past promotions, directly outputs a predicted replica count (e.g., `{"predicted_replicas": 8}`).
    *   The `smart-provisioning.md` logic receives this prediction and executes `kubectl scale deployment <web-app> --replicas=8`.
*   **Simulate Surge & Monitor:** Load is applied; performance is monitored.
*   **Observe Scale Down:** After the surge (and potentially a cooldown period, or based on a new prediction indicating normal load), the LLM is queried again with current metrics. It predicts the baseline replica count (e.g., `{"predicted_replicas": 2}`), and the provisioning logic scales the deployment down.

## 2. Retrieval-Augmented Generation (RAG) Approach

*   **Setup:** A general-purpose LLM is used. A vector database is populated with embeddings of historical monitoring data chunks, incident reports, and documentation related to past traffic surges and the application's behavior.
*   **Trigger Prediction:** A prompt is constructed like: "Predict the required replica count for 'webapp-deployment' in the next hour, considering the current metrics [current CPU, Mem, request rate] and the upcoming event 'marketing_campaign_X'. Justify your prediction."
*   **Observe Proactive Scaling:**
    *   The RAG system retrieves relevant documents/data chunks (e.g., metrics from the last 'marketing_campaign_X', performance reports mentioning scaling issues during similar events).
    *   This retrieved context is added to the prompt and sent to the LLM via the `prediction-api.md`.
    *   The LLM generates a response, including the predicted replica count (e.g., "Based on the last campaign X which saw a 5x traffic increase handled by 7 replicas, and current baseline load, I recommend scaling to 8 replicas.").
    *   The `smart-provisioning.md` logic parses this response (or a structured output part) and executes the scaling command.
*   **Simulate Surge & Monitor:** Load is applied; performance is monitored.
*   **Observe Scale Down:** A similar RAG query is made after the surge, retrieving context about post-event traffic levels, leading the LLM to predict scaling down.

## 3. AI Agent (Single Agent) Approach

*   **Setup:** A single agent is configured with access to tools: a monitoring data reader (`data-collection.md`), the LLM prediction API (`prediction-api.md` - could be fine-tuned or RAG-based internally), and a Kubernetes interaction tool (`k8s-integration.md`). Its goal is to maintain application performance efficiently.
*   **Trigger Prediction:** The agent continuously observes metrics. It detects the "upcoming event" flag or notices patterns indicative of an impending surge based on its internal LLM reasoning.
*   **Observe Proactive Scaling:**
    *   The agent's internal LLM decides a scaling action is needed based on the prediction.
    *   The agent plans the action: "Query LLM for predicted replicas for 'webapp-deployment' given event 'marketing_campaign_X'".
    *   It receives the prediction (e.g., 8 replicas).
    *   It plans and executes the next action: "Use Kubernetes tool to scale 'webapp-deployment' to 8 replicas".
*   **Simulate Surge & Monitor:** Load is applied. The agent continues monitoring, potentially making minor adjustments if its initial prediction was slightly off.
*   **Observe Scale Down:** After the surge, the agent observes metrics returning to normal. Its LLM determines scaling down is appropriate, and it plans and executes the scale-down action using its Kubernetes tool.

## 4. Multi-Agent System (MAS) Approach

*   **Setup:** Specialized agents are deployed: Monitoring Agent, Prediction Agent (using LLM/RAG), Provisioning Agent.
*   **Trigger Prediction:**
    *   The Monitoring Agent detects the upcoming event flag and gathers current metrics.
    *   It sends this data package to the Prediction Agent.
*   **Observe Proactive Scaling:**
    *   The Prediction Agent uses its LLM (fine-tuned or RAG) to determine the required replica count (e.g., 8).
    *   It sends a command/request to the Provisioning Agent: `{"action": "scale", "target": "webapp-deployment", "replicas": 8}`.
    *   The Provisioning Agent validates the request and executes the `kubectl scale` command via `k8s-integration.md`.
*   **Simulate Surge & Monitor:** Load is applied. The Monitoring Agent continues sending data; the Prediction Agent might send updates if needed.
*   **Observe Scale Down:**
    *   Monitoring Agent reports normal metrics post-surge.
    *   Prediction Agent determines baseline replicas are sufficient (e.g., 2).
    *   Prediction Agent sends scale-down command (`{"action": "scale", "target": "webapp-deployment", "replicas": 2}`) to the Provisioning Agent.
    *   Provisioning Agent executes the scale-down.

Each approach achieves the scenario's goal but differs in implementation complexity, data requirements, and the degree of autonomy.