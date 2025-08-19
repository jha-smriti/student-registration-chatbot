export type ChatRequest = { session_id: string; message: string };
export type ChatResponse = {
reply: string;
intent: string;
confidence: number;
entities: Record<string, string>;
suggestions?: string[];
};