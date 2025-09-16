import { useState } from "react";
import "./form.scss";
export function Form() {
  const [text, setText] = useState("");
  const [result, setResult] = useState("");

  const handlePredict = async () => {
    if (!text.trim()) {
      alert("Please enter some text!");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();
      if (data.sentiment) {
        setResult(data.sentiment);
      } else {
        setResult("Error: " + data.error);
      }
    } catch (error) {
      setResult("Server error. Is backend running?");
    }
  };
  return (
    <div className="container">
      <h1>🧠 MindMoods Sentiment Classifier</h1>
      <textarea
        rows={4}
        placeholder="Type your text here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      ></textarea>
      <button onClick={handlePredict}>Predict Sentiment 🔍</button>
      {result && (
        <h2>
          Sentiment:{" "}
          <span
            style={{
              color:
                result === "positive"
                  ? "green"
                  : result === "negative"
                  ? "red"
                  : "orange",
            }}
          >
            {result}
          </span>
        </h2>
      )}
    </div>
  );
}
