<template>
  <div class="container">
    <div class="article-detail" v-if="article">
      <header>
        <h1>{{ article.title }}</h1>
        <div class="meta">
          <span class="date">{{ formatDate(article.created_at) }}</span>
          <div class="labels">
            <span v-for="label in article.labels" :key="label" class="label">
              {{ label }}
            </span>
          </div>
        </div>
      </header>
      <main>
        <div class="markdown-body" v-html="markdownToHtml(article.content)"></div>
        <div class="source">
          <a :href="article.url" target="_blank">查看原文</a>
        </div>
      </main>
      <div class="image-preview" v-if="previewImage" @click="closePreview">
        <img :src="previewImage" alt="preview" >
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { marked } from 'marked'
import articles from '../data/articles.json'

const props = defineProps<{
  id: string
}>()

const article = computed(() => 
  articles.find(a => a.id === parseInt(props.id)) //

)

const formatDate = (dateStr: string) => {
  return new Date(dateStr).toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

const previewImage = ref<string | null>(null)

const handleImageClick = (event: MouseEvent) => {
  const target = event.target as HTMLImageElement
  if (target.tagName === 'IMG') {
    previewImage.value = target.src
    document.body.style.overflow = 'hidden'
    // 添加 referrerpolicy="no-referrer"
    target.setAttribute('referrerpolicy', 'no-referrer')
  }
}

const closePreview = () => {
  previewImage.value = null
  document.body.style.overflow = ''
}

const markdownToHtml = (content: string) => {
  marked.setOptions({
    breaks: true,
    gfm: true,
    headerIds: true,
    mangle: false,
    sanitize: false,
  })
  
  const html = marked(content)
  return html.replace(
    /<img\s+src="([^"]+)"/g, 
    '<div class="article-img-wrapper"><div class="img-container"><img src="$1" loading="lazy" referrerpolicy="no-referrer" onclick="window.handleImageClick(event)"'
  )
}

window.handleImageClick = handleImageClick
</script>

<style scoped>
.container {
  max-width: 75%;
  margin: 0 auto;
  padding: 24px;
  min-height: calc(100vh - 64px);
}

h1 {
  font-size: 1.75rem;
  font-weight: 600;
  color: #111827;
  margin-bottom: 16px;
  line-height: 1.3;
  letter-spacing: -0.025em;
}

.meta {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin: 16px 0;
}

.date {
  color: #6b7280;
  font-size: 0.875rem;
}

.labels {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.label {
  padding: 4px 12px;
  border-radius: 16px;
  font-size: 12px;
  font-weight: 500;
  color: #16a34a;
  background: #dcfce7;
  transition: all 0.2s ease;
  cursor: default;
  display: inline-flex;
  align-items: center;
  line-height: 1.2;
}

.label:hover {
  background: #bbf7d0;
}

main {
  background: white;
  padding: 32px;
  border-radius: 16px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  border: 1px solid #f0f0f0;
}

.markdown-body {
  color: #374151;
  line-height: 1.8;
  font-size: 1rem;
}
/*
.markdown-body >>> img {
  width: 100%;
}
*/
.markdown-body p {
  margin: 1.2em 0;
  line-height: 1.7;
}

.markdown-body h1,
.markdown-body h2,
.markdown-body h3,
.markdown-body h4 {
  color: #111827;
  font-weight: 600;
  margin: 1.5em 0 1em;
  line-height: 1.3;
}

.markdown-body h1 { font-size: 1.5rem; }
.markdown-body h2 { font-size: 1.375rem; }
.markdown-body h3 { font-size: 1.25rem; }
.markdown-body h4 { font-size: 1.125rem; }

.markdown-body pre {
  background: #f8fafc;
  padding: 16px;
  border-radius: 8px;
  overflow-x: auto;
  margin: 1.5em 0;
  border: 1px solid #e5e7eb;
  font-size: 0.9375rem;
}

.markdown-body code {
  font-family: ui-monospace, monospace;
  color: #374151;
}

.markdown-body blockquote {
  margin: 1.5em 0;
  padding: 0.5em 1em;
  border-left: 4px solid #e5e7eb;
  background: #f9fafb;
  color: #4b5563;
}

.source {
  margin-top: 24px;
  padding-top: 16px;
  border-top: 1px solid #f3f4f6;
  display: flex;
  justify-content: flex-end;
}

.source a {
  font-size: 0.875rem;
  color: #2563eb;
  font-weight: 500;
  text-decoration: none;
}

.source a:hover {
  text-decoration: underline;
}

.image-preview {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.9);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  cursor: zoom-out;
}

.image-preview img {
  max-width: 90%;
  max-height: 90vh;
  object-fit: contain;
  border-radius: 8px;
}

@media screen and (max-width: 768px) {
  .container {
    max-width: 100%;
    padding: 16px;
  }

  h1 {
    font-size: 1.25rem;
    margin-bottom: 12px;
  }

  .markdown-body h1 { font-size: 1.25rem; }
  .markdown-body h2 { font-size: 1.125rem; }
  .markdown-body h3 { font-size: 1rem; }
  .markdown-body h4 { font-size: 0.938rem; }
}

@media screen and (max-width: 480px) {
  .container {
    padding: 12px 8px;
  }

  h1 {
    font-size: 1.125rem;
  }

  main {
    padding: 12px;
  }

  .markdown-body {
    font-size: 0.875rem;
  }

  .image-preview img {
    max-width: 95%;
    max-height: 95vh;
  }

  .labels {
    margin: 8px 0;
  }

  .source {
    margin-top: 16px;
    padding-top: 12px;
  }
}
</style> 