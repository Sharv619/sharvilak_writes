# Implementation Plan: Creative Consciousness RAG System

This plan outlines the steps to build a Retrieval-Augmented Generation (RAG) system using the user's creative writing archive (2017-2022) from WordPress and Instagram.

## Objective
To capture the user's "creative consciousness" by embedding their historical writings into a vector database (ChromaDB) and providing a chat interface that uses these embeddings for context-aware responses.

## Key Files & Context
- `knowledge_base/himanshoe.WordPress.2026-04-30.xml`: Source WordPress data.
- `knowledge_base/wordpress_ig_context.json`: Pre-extracted structured data.
- `knowledge_base/scraped_posts/`: Local copies of Instagram posts/metadata.
- `knowledge_base/scripts/`: Existing scripts for reference.

## Implementation Steps

### 1. Environment Setup
- Install required dependencies:
  - `langchain` & `langchain-community`: For RAG orchestration.
  - `langchain-google-genai` (or `openai`): For embeddings and LLM.
  - `chromadb`: For vector storage.
  - `beautifulsoup4`, `lxml`: For robust XML/HTML parsing.
  - `python-dotenv`: For managing API keys.

### 2. Data Extraction & Preprocessing
- Create a new script `knowledge_base/scripts/build_vector_store.py`.
- Implement a `ContentExtractor` to:
  - Parse the WordPress XML for all `<item>` entries where `wp:post_type` is `post` and status is `publish`.
  - Extract titles, dates, and full HTML content.
  - Clean HTML tags and WordPress shortcodes.
  - Integrate data from `wordpress_ig_context.json` and `scraped_posts` metadata (captions).
- Organize the data into `Document` objects with metadata (source, date, title).

### 3. Chunking & Embedding
- Use a `RecursiveCharacterTextSplitter` to break long creative pieces into manageable chunks (e.g., 500-1000 characters with 10% overlap).
- Initialize the embedding model (e.g., `GoogleGenerativeAIEmbeddings`).
- Create and persist a ChromaDB collection in `knowledge_base/vector_db/`.

### 4. RAG Interface (CLI & Django)
- Create a reusable `RAGChain` component using LangChain's `RetrievalQA` or `create_retrieval_chain`.
- **CLI Tool:** A simple script `chat_with_me.py` for immediate interaction.
- **Django Integration:** 
  - Add a new view in `blog/views.py` (e.g., `CreativeChatView`).
  - Add a corresponding URL pattern and a simple template for a chat-like interface.

## Verification & Testing
- **Data Check:** Verify the number of documents/chunks indexed matches the source data.
- **Retrieval Test:** Query the vector store for specific unique phrases from old posts to ensure high relevance.
- **End-to-End Test:** Ask the chatbot questions about specific themes or events described in the writings (e.g., "What was the story behind the letter to Kiara?").

## Future Considerations
- Fine-tuning the prompt to better capture the specific "voice" or "consciousness" of the creative writings.
- Adding a "memory" component to the chat so it remembers the current conversation context.
- Expanding the knowledge base with new blog posts as they are written.

---

# Work Breakdown Structure (WBS): Creative Consciousness RAG

This WBS decomposes the "Creative Consciousness" RAG system into manageable work packages.

## 1. Project Initialization & Environment
- **1.1. Dependency Management**
    - 1.1.1. Identify and document required libraries (LangChain, ChromaDB, BeautifulSoup, etc.)
    - 1.1.2. Update `requirements.txt`
    - 1.1.3. Set up `.env` for API keys (Gemini/OpenAI)
- **1.2. Knowledge Base Audit**
    - 1.2.1. Verify integrity of WordPress XML file
    - 1.2.2. Map Instagram scraped media to metadata captions
    - 1.2.3. Consolidate `wordpress_ig_context.json` with raw sources

## 2. Data Engineering & Pipeline
- **2.1. WordPress Parser**
    - 2.1.1. Develop XML parser for `<item>` extraction
    - 2.1.2. Implement HTML cleaning (strip tags, handle entities)
    - 2.1.3. Extract metadata (Title, Date, Category, Slug)
- **2.2. Instagram Parser**
    - 2.2.1. Extract captions from `.json` or `.txt` sidecar files in `scraped_posts/`
    - 2.2.2. Standardize metadata format to match WordPress entries
- **2.3. Data Normalization**
    - 2.3.1. Merge all sources into a unified Document format
    - 2.3.2. Deduplicate overlapping content (e.g., cross-posts)

## 3. Vectorization & Storage
- **3.1. Document Chunking**
    - 3.1.1. Configure `RecursiveCharacterTextSplitter` (chunk size/overlap)
    - 3.1.2. Validate chunk integrity (ensure stories aren't cut mid-sentence)
- **3.2. Embedding Generation**
    - 3.2.1. Configure Embedding model (Gemini or OpenAI)
    - 3.2.2. Batch process chunks through the embedding API
- **3.3. ChromaDB Persistence**
    - 3.3.1. Initialize local ChromaDB collection
    - 3.3.2. Upsert vectors and metadata
    - 3.3.3. Verify storage persistence in `knowledge_base/vector_db/`

## 4. RAG Logic & Personas
- **4.1. Retrieval Optimization**
    - 4.1.1. Implement similarity search logic
    - 4.1.2. Test retrieval relevance for key themes (Romance, Fiction, etc.)
- **4.2. Prompt Engineering**
    - 4.2.1. Design System Prompt to capture "Creative Consciousness" voice
    - 4.2.2. Implement context-injection templates
- **4.3. Chat Logic**
    - 4.3.1. Build LangChain Retrieval Chain
    - 4.3.2. Add conversation memory (Buffer or Summary)

## 5. Interface & Integration
- **5.1. CLI Tooling**
    - 5.1.1. Develop `scripts/chat_consciousness.py`
    - 5.1.2. Implement streaming output
- **5.2. Django Web Integration**
    - 5.2.1. Create `CreativeChatView` in `blog/views.py`
    - 5.2.2. Design chat UI in `blog/templates/blog/chat.html`
    - 5.2.3. Wire up URL routing

## 6. Testing & Validation
- **6.1. Content Fidelity Test**
    - 6.1.1. Ask questions about specific 2017-2022 events/characters
- **6.2. Voice Consistency Test**
    - 6.2.1. Evaluate if responses match the user's creative writing style
- **6.3. System Performance**
    - 6.3.1. Measure latency for retrieval and generation
