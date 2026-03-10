# Course 06: Essentials and Applications of Generative AI - Lesson outlines

## Lesson 44: State of the art in generative AI (Foundation overview)

**Focus:** Survey of state-of-the-art large language models for text and code generation

| Topic | Purpose |
|-------|--------|
| Open vs closed weights | Distinction between API-only and self-hostable models |
| Text generation models | GPT, Claude, Gemini, Llama, Mistral - capabilities and use cases |
| Code generation models | Qwen, CodeLlama, StarCoder, DeepSeek Coder - programming assistance |
| Key trends | Longer context windows, efficiency improvements, open model progress, specialization |
| Limitations and considerations | Hallucinations, costs, privacy concerns, bias, copyright |

**Key concepts:** Open vs closed weights, foundation models, LLM landscape, practical applications

---

## Lesson 45: Text generation with LLMs (Practical deployment)

**Focus:** Deployment strategies and practical considerations for working with LLMs

| Topic | Purpose |
|-------|--------|
| How model interaction works | Input/output text flow, conversation context |
| Self-hosting locally | Running models on local hardware (Ollama, llama.cpp, GPT4All, LM Studio) |
| Self-hosting in cloud | Deploying on cloud infrastructure (AWS SageMaker, RunPod, vLLM) |
| API access | Using hosted APIs (OpenAI, Anthropic, Google) |
| Performance and cost tradeoffs | Latency, throughput, quality, and cost comparison across deployment options |
| Decision framework | Choosing deployment based on privacy, volume, and quality needs |
| LLM application frameworks | LangChain, LlamaIndex, Haystack, Semantic Kernel, DSPy |

**Builds on 44:** Applies foundation model knowledge to practical implementation

**Key concepts:** Deployment strategies, cost-benefit analysis, model hosting options, application frameworks

---

## Lesson 46: Advanced prompt engineering techniques: Part 1 (Prompting strategies)

**Focus:** Fundamental prompting approaches for eliciting better LLM responses

| Topic | Purpose |
|-------|---------|
| Zero-shot prompting | Task completion without examples |
| Few-shot prompting | Learning from in-context examples |
| Prompt structure | Role definitions, temperature settings |
| Practical examples | Translation, classification, text analysis |

**Builds on 45:** Uses LLM APIs learned previously, focuses on prompt design

**Key concepts:** In-context learning, example-based prompting, prompt engineering fundamentals

---

## Lesson 47: Advanced prompt engineering techniques: Part 2 (Advanced reasoning)

**Focus:** Sophisticated prompting techniques for complex reasoning tasks

| Topic | Purpose |
|-------|---------|
| Chain of thought (CoT) | Step-by-step reasoning prompts |
| Self-consistency | Multiple reasoning paths, majority voting |
| Tree of thoughts (ToT) | Branching reasoning, exploration of solution space |
| Template formats | Jinja2 templates, f-strings, custom templates |
| Dynamic message generation | Programmatic prompt construction |

**Builds on 46:** Extends basic prompting to complex multi-step reasoning

**Key concepts:** Reasoning chains, multi-path exploration, dynamic prompt generation

---

## Lesson 48: LangChain for LLM application development: Part 1 (Core components)

**Focus:** Building blocks of LangChain applications

| Topic | Purpose |
|-------|---------|
| Models | Chat models, LLM wrappers, direct API calls |
| Prompts | ChatPromptTemplate, structured prompts |
| Output parsers | Structured output extraction, format control |
| Basic chains | Connecting models, prompts, and parsers |

**Builds on 47:** Formalizes prompt engineering with LangChain abstractions

**Key concepts:** Model-Prompt-Parser pipeline, LangChain component architecture

---

## Lesson 49: LangChain for LLM application development: Part 2 (Advanced patterns)

**Focus:** Retrieval, memory, and autonomous agents

| Topic | Purpose |
|-------|---------|
| Document loaders | TextLoader, PyPDFLoader for various formats |
| Text splitters | RecursiveCharacterTextSplitter for chunking |
| Embeddings | HuggingFace and OpenAI embeddings |
| Vector stores | Chroma for similarity search and persistence |
| Sequential chains | Multi-step workflows with context passing |
| Memory | Conversation history, state management |
| Agents | Autonomous tool use (llm-math, wikipedia) |
| Local LLMs | Running Falcon models locally |

**Builds on 48:** Extends basic chains to RAG, memory, and agent patterns

**Key concepts:** Retrieval-augmented generation (RAG), vector databases, autonomous agents

---

## Lesson 50: LLM fine-tuning, customization, and tool integration (Model adaptation)

**Focus:** Adapting pre-trained models and extending capabilities with tools

| Topic | Purpose |
|-------|---------|
| Data preparation | Dataset formatting, preprocessing for fine-tuning |
| Fine-tuning techniques | LoRA, QLoRA for parameter-efficient fine-tuning |
| Domain adaptation | Adapting models to specific domains (legal, medical, etc.) |
| Evaluation | Assessing fine-tuned model performance |
| Model Context Protocol (MCP) | Standardized protocol for LLM-tool communication |
| MCP servers | Building and deploying MCP servers for custom tools |
| Tool integration | Connecting LLMs to external APIs, databases, and services |
| Function calling | Structured tool use with modern LLMs |

**Builds on 49:** Extends agent capabilities with custom tools and domain-specific models

**Key concepts:** Transfer learning, parameter-efficient fine-tuning, tool integration protocols, MCP architecture

---

## Lesson 51: Advanced agents and production deployment

**Focus:** Complex multi-agent systems and deploying LLM applications to production

| Topic | Purpose |
|-------|---------|
| Multi-agent architectures | Coordinating multiple specialized agents |
| Agent planning | ReAct, reflection, and iterative refinement patterns |
| Agent memory systems | Long-term memory, knowledge graphs for agents |
| Evaluation frameworks | Testing agent reliability and performance |
| Production deployment | Containerization, API design, monitoring |
| Cost optimization | Caching, prompt optimization, model selection |
| Safety and alignment | Guardrails, content filtering, output validation |

**Builds on 50:** Advanced patterns building on basic agents from Lesson 49

**Key concepts:** Multi-agent coordination, production engineering, safety considerations, deployment best practices

---

## Course progression summary

1. **Foundation (Lesson 44):** State-of-the-art generative AI landscape  
2. **LLM Deployment (Lesson 45):** Local hosting, cloud hosting, API access  
3. **Prompt Engineering (Lessons 46-47):** Zero-shot → Few-shot → CoT → ToT  
4. **LangChain Development (Lessons 48-49):** Core components → RAG + Agents  
5. **Customization & Tools (Lesson 50):** Fine-tuning, MCP servers, tool integration  
6. **Advanced Production (Lesson 51):** Multi-agent systems, deployment, safety
