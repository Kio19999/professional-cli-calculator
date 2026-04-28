const { test, expect } = require('@playwright/test');

test('login page loads', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/login-page');
  await expect(page.locator('h1')).toHaveText('Login');
});

test('register page loads', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/register-page');
  await expect(page.locator('h1')).toHaveText('Register');
});