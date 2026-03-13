export function register(pluginManager) {
  pluginManager.addRoute({
    path: '/monitoring',
    name: 'Monitoring',
    component: () => import('./views/MonitoringView.vue'),
    meta: { requiresAuth: true }
  })

  pluginManager.addMenu({
    title: 'Мониторинг',
    icon: 'ChartBarIcon',
    path: '/monitoring'
  })
}