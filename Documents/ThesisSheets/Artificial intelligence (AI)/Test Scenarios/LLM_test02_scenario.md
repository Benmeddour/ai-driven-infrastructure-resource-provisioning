# Test Scenario: LLM-Assisted Initial Resource Sizing

This scenario focuses on leveraging the LLM during the initial deployment phase of a new application to predict appropriate starting resource configurations (replicas, CPU/Memory requests/limits).

**Goal:** Verify that the LLM can provide sensible initial resource sizing recommendations for a new Kubernetes application based on its characteristics, aiming to prevent immediate under-provisioning (leading to instability) or significant over-provisioning (wasting resources) upon first launch.

**Scenario:** A developer is about to deploy a *new* microservice (e.g., a Python/FastAPI backend API) to the Kubernetes cluster. Instead of manually guessing the initial `replicas`, `resources.requests`, and `resources.limits`, the deployment process consults the LLM.

**System Components Involved:**
*   **LLM Prediction Model:** Trained/fine-tuned to predict resource needs based on application metadata (type, framework, language) and potentially historical data from similar deployments. (Ref: `../llm-driven-operations/model-training.md`)
*   **Prediction API:** Accepts application metadata and returns predicted sizing parameters. (Ref: `../llm-driven-operations/prediction-api.md`)
*   **Smart Provisioning / Integration:** Logic (potentially in CI/CD or an admission controller) that queries the LLM before deployment and uses the prediction to populate the manifest. (Ref: `../llm-driven-operations/smart-provisioning.md`, `../llm-driven-operations/k8s-integration.md`)
*   **(Optional) Monitoring Data:** Historical data from previously deployed applications used for training the LLM. (Ref: `../llm-driven-operations/data-collection.md`)

**Test Steps:**

1.  **Setup:**
    *   Ensure the LLM model is trained/configured for initial sizing predictions.
    *   Ensure the prediction API is ready to receive application metadata.
    *   Set up the integration point (e.g., a script in a CI/CD pipeline, a manual query step) to call the LLM before `kubectl apply`.
2.  **Define New Application:**
    *   Prepare the Kubernetes Deployment manifest for the new application (e.g., `new-fastapi-service`). Leave `replicas`, `resources.requests`, and `resources.limits` unspecified or set to placeholder values.
    *   Identify the key metadata for the LLM (e.g., `{"app_type": "backend_api", "language": "python", "framework": "fastapi"}`).
3.  **Trigger Initial Sizing Prediction:**
    *   Execute the process that sends the metadata to the LLM prediction API.
4.  **Observe LLM Output:**
    *   Record the predicted values returned by the LLM (e.g., `replicas: 2`, `requests: {"cpu": "250m", "memory": "256Mi"}`, `limits: {"cpu": "500m", "memory": "512Mi"}`).
5.  **Deploy with Predicted Sizing:**
    *   Update the Deployment manifest with the LLM's predicted values.
    *   Deploy the application to Kubernetes (`kubectl apply -f deployment.yaml`).
6.  **Apply Initial Baseline Load:**
    *   Once the pods are ready, generate a small, steady stream of traffic representative of expected initial usage (e.g., a few requests per second).
7.  **Monitor Initial Stability & Performance:**
    *   Verify the pods started successfully without crashing (e.g., OOMKilled) or excessive restarts.
    *   Check for immediate CPU throttling events.
    *   Measure application response times and error rates under the baseline load. Are they within acceptable limits?
    *   Observe the actual CPU and Memory usage of the pods. How does it compare to the LLM-predicted requests? Is there comfortable headroom below the limits?
8.  **(Optional) Comparison:** Deploy the same application again, but this time using default resource values or a manual best guess, and compare its initial stability, performance, and resource utilization against the LLM-sized deployment under the same baseline load.

**Variables/Metrics to Test/Monitor:**

*   **Input Metadata (to LLM):** Application type, language, framework, etc.
*   **LLM Prediction Output:** Predicted `replicas`, `requests.cpu`, `requests.memory`, `limits.cpu`, `limits.memory`.
*   **Deployment Success:** Pods scheduled, containers running, readiness probes passing.
*   **Initial Stability:** Container restarts, OOMKilled events, CPU Throttling.
*   **Initial Performance (Baseline Load):** Average response time, error rate.
*   **Resource Utilization (Baseline Load):** Actual pod CPU/Memory usage vs. requested/limited amounts.

This scenario validates the LLM's utility in the critical initial deployment phase, potentially streamlining operations and improving resource efficiency from the moment an application goes live.