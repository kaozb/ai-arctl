<template>
  <nav class="nav">
    <div class="nav-container">
      <router-link to="/" class="nav-logo">
        博客保存
      </router-link>
      <div class="nav-links">
        <label class="toggle-switch">
          <input type="checkbox" v-model="fullShow" id="fullShow">
          <span class="slider"></span>
          <span class="label-text">{{ fullShow ? '分页' : '滚动' }}</span>
        </label>
        <a href="https://github.com/kaozb/ai-arctl/issues" target="_blank" class="nav-link github-link">
          <svg height="24" width="24" viewBox="0 0 16 16" class="github-icon">
            <path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
          </svg>
        </a>
      </div>
    </div>
  </nav>
  <router-view v-model:fullShow="fullShow"></router-view>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const fullShow = ref(false)
</script>

<style>
.nav {
  background: #f9fafb;
  border-bottom: 1px solid #f0f0f0;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-logo {
  font-size: 1.25rem;
  font-weight: 600;
  color: #111827;
  text-decoration: none;
  letter-spacing: -0.025em;
}

.nav-links {
  display: flex;
  align-items: center;
}

.nav-link {
  color: #4b5563;
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 500;
  transition: color 0.2s ease;
}

.nav-link:hover {
  color: #2563eb;
}

.nav-link.router-link-active {
  color: #2563eb;
}

@media screen and (max-width: 768px) {
  .nav {
    width: 100%;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
  }

  .nav-container {
    height: 56px;
    padding: 0 16px;
    width: 100%;
    box-sizing: border-box;
  }

  .nav-logo {
    font-size: 1.125rem;
  }

  .github-link svg {
    height: 20px;
    width: 20px;
  }
}

@media screen and (max-width: 480px) {
  #app {
    padding-top: 56px;
  }

  .nav-container {
    padding: 0 12px;
  }
}

.toggle-switch {
  position: relative;
  display: inline-flex;
  align-items: center;
  cursor: pointer;
  margin-right: 16px;
}

.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: relative;
  display: inline-block;
  width: 40px;
  height: 20px;
  background-color: #e5e7eb;
  border-radius: 20px;
  transition: .4s;
  margin-right: 8px;
}

.slider:before {
  position: absolute;
  content: "";
  height: 16px;
  width: 16px;
  left: 2px;
  bottom: 2px;
  background-color: white;
  border-radius: 50%;
  transition: .4s;
}

.toggle-switch input:checked + .slider {
  background-color: #2563eb;
}

.toggle-switch input:checked + .slider:before {
  transform: translateX(20px);
}

.label-text {
  font-size: 14px;
  color: #6b7280;
  white-space: nowrap;
}

@media screen and (max-width: 768px) {
  .label-text {
    display: none;
  }
  
  .toggle-switch {
    margin-right: 12px;
  }
}
</style> 