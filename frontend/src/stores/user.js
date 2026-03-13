import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    token: localStorage.getItem('access_token'),
    theme: localStorage.getItem('theme') || 'dark'
  }),
  actions: {
    setToken(token) {
      this.token = token
      localStorage.setItem('access_token', token)
    },
    logout() {
      this.user = null
      this.token = null
      localStorage.removeItem('access_token')
    },
    toggleTheme() {
      this.theme = this.theme === 'dark' ? 'light' : 'dark'
      localStorage.setItem('theme', this.theme)
      document.documentElement.classList.toggle('dark', this.theme === 'dark')
    }
  }
})