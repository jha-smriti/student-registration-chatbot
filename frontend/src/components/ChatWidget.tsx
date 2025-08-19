import React, { useRef, useState, useEffect } from "react";
import styled from "styled-components";
import api from "../api/client";
import { ChatRequest, ChatResponse } from "../types";
const Wrapper = styled.div position: fixed; bottom: 24px; right: 24px; width: 360px; max-height: 70vh; border: 1px solid #e2e8f0; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.12); background: #fff; display: flex; flex-direction: column;;

const Header = styled.div background: #2563eb; color: #fff; padding: 12px 16px; font-weight: 600;;

const Messages = styled.div padding: 12px; overflow-y: auto; flex: 1;;

const InputRow = styled.form display: flex; gap: 8px; padding: 12px; border-top: 1px solid #e5e7eb;;

const Input = styled.input flex: 1; padding: 10px 12px; border: 1px solid #e5e7eb; border-radius: 8px; outline: none;;

const SendBtn = styled.button background: #2563eb; color: #fff; border: 0; padding: 10px 12px; border-radius: 8px; cursor: pointer;;

type Message = { id: string; role: "user" | "bot"; text: string };

const ChatWidget: React.FC = () => {
const [messages, setMessages] = useState<Message[]>([
{ id: "welcome", role: "bot", text: "Hi! I can help with registration dates, required documents, fee payment, and portal steps." }
]);
const [input, setInput] = useState("");
const [loading, setLoading] = useState(false);
const sessionId = useRef<string>(crypto.randomUUID());

const onSubmit = async (e: React.FormEvent) => {
e.preventDefault();
if (!input.trim()) return;
const userMsg: Message = { id: crypto.randomUUID(), role: "user", text: input };
setMessages((m) => [...m, userMsg]);
setInput("");
setLoading(true);
try {
const payload: ChatRequest = { session_id: sessionId.current, message: userMsg.text };
const { data } = await api.post<ChatResponse>("/chat", payload);
const botMsg: Message = { id: crypto.randomUUID(), role: "bot", text: data.reply };
setMessages((m) => [...m, botMsg]);
} catch {
setMessages((m) => [...m, { id: crypto.randomUUID(), role: "bot", text: "Sorry, something went wrong." }]);
} finally {
setLoading(false);
}
};

useEffect(() => {
const el = document.getElementById("chat-messages");
if (el) el.scrollTop = el.scrollHeight;
}, [messages]);

return (
<Wrapper>
<Header>Registration Assistant</Header>
<Messages id="chat-messages">
{messages.map((m) => (
<div key={m.id} style={{ display: "flex", justifyContent: m.role === "user" ? "flex-end" : "flex-start", marginBottom: 8 }}>
<div style={{ background: m.role === "user" ? "#2563eb" : "#f3f4f6", color: m.role === "user" ? "#fff" : "#111827", padding: "8px 10px", borderRadius: 10, maxWidth: "80%" }}>
{m.text}
</div>
</div>
))}
{loading && <div style={{ color: "#6b7280", fontSize: 12 }}>Typing…</div>}
</Messages>
<InputRow onSubmit={onSubmit}>
<Input placeholder="Ask about registration…" value={input} onChange={(e) => setInput(e.target.value)} />
<SendBtn type="submit">Send</SendBtn>
</InputRow>
</Wrapper>
);
};

export default ChatWidget;