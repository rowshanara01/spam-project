"use client";
// Step 3: Next.js frontend. eta web/app/page.tsx e rakho.
import { useState } from "react";

type Result = { label: "spam" | "ham"; spam_probability: number };

export default function Home() {
  const [text, setText] = useState("");
  const [result, setResult] = useState<Result | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function check() {
    setLoading(true);
    setError("");
    try {
      const res = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      if (!res.ok) throw new Error("API error");
      setResult(await res.json());
    } catch {
      setError("API connect hocche na. Backend cholche to?");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main style={{ maxWidth: 520, margin: "40px auto", padding: 16 }}>
      <h1>Spam Detector</h1>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={5}
        style={{ width: "100%", padding: 8 }}
        placeholder="Ekta message likho..."
      />
      <button onClick={check} disabled={!text.trim() || loading}>
        {loading ? "Checking..." : "Check"}
      </button>
      {error && <p style={{ color: "crimson" }}>{error}</p>}
      {result && (
        <p>
          Result: <b>{result.label.toUpperCase()}</b> (spam probability:{" "}
          {(result.spam_probability * 100).toFixed(1)}%)
        </p>
      )}
    </main>
  );
}
