
const API_BASE_URL = "http://127.0.0.1:8000";

const form = document.getElementById("validationForm");
const button = document.getElementById("validateButton");
const loading = document.getElementById("loading");
const errorBox = document.getElementById("error");
const resultBox = document.getElementById("result");

async function apiRequest(endpoint, options = {}) {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        ...options,
        headers: {
            "Content-Type": "application/json",
            ...options.headers
        }
    });

    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.detail || "API request failed");
    }

    return data;
}

async function checkAPI() {
    const status = document.getElementById("apiStatus");

    try {
        await apiRequest("/health");
        status.textContent = "API Connected";
    } catch {
        status.textContent = "API Disconnected";
    }
}

async function loadSummary() {
    try {
        const data = await apiRequest("/history/summary");

        document.getElementById("total").textContent =
            data.total_validations ?? 0;

        document.getElementById("successful").textContent =
            data.successful_validations ?? 0;

        document.getElementById("failed").textContent =
            data.failed_validations ?? 0;

        document.getElementById("successRate").textContent =
            `${data.success_rate ?? 0}%`;

    } catch (error) {
        console.error("Summary error:", error);
    }
}

async function loadHistory() {
    const historyList = document.getElementById("historyList");

    historyList.textContent = "Loading history...";

    try {
        const data = await apiRequest("/history");

        historyList.replaceChildren();

        if (!data.history || data.history.length === 0) {
            historyList.textContent = "No validation records found.";
            return;
        }

        data.history.forEach(item => {
            const report = item.report || {};

            const container = document.createElement("div");
            container.className = "history-item";

            const title = document.createElement("strong");
            title.textContent = report.project_path || "Unknown project";

            const details = document.createElement("div");
            details.textContent =
                `Status: ${report.status || "Unknown"} | ` +
                `Score: ${report.score || "N/A"} | ` +
                `Date: ${item.timestamp || "N/A"}`;

            container.append(title, details);
            historyList.appendChild(container);
        });

    } catch (error) {
        historyList.textContent =
            `Unable to load history: ${error.message}`;
    }
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    if (button.disabled) return;

    const projectPath =
        document.getElementById("projectPath").value.trim();

    if (!projectPath) return;

    button.disabled = true;
    loading.hidden = false;
    errorBox.hidden = true;
    resultBox.replaceChildren();

    try {
        const data = await apiRequest("/validate", {
            method: "POST",
            body: JSON.stringify({
                project_path: projectPath
            })
        });

        const report = data.validation;

        const result = document.createElement("div");
        result.className = "result";

        const heading = document.createElement("h3");
        heading.className = report.status;
        heading.textContent = `Status: ${report.status}`;

        const score = document.createElement("p");
        score.textContent =
            `Validation Score: ${report.score} (${report.percentage}%)`;

        const message = document.createElement("p");
        message.textContent = report.message;

        const list = document.createElement("ul");

        Object.entries(report.checks || {}).forEach(([name, passed]) => {
            const item = document.createElement("li");
            item.textContent =
                `${passed ? "✓" : "✗"} ${name}: ${passed ? "PASS" : "FAIL"}`;
            list.appendChild(item);
        });

        result.append(heading, score, message, list);
        resultBox.appendChild(result);

        await Promise.all([loadSummary(), loadHistory()]);

    } catch (error) {
        errorBox.textContent = `Validation failed: ${error.message}`;
        errorBox.hidden = false;

    } finally {
        loading.hidden = true;
        button.disabled = false;
    }
});

document.getElementById("refreshButton").addEventListener(
    "click",
    () => Promise.all([loadSummary(), loadHistory()])
);

checkAPI();
loadSummary();
loadHistory();
