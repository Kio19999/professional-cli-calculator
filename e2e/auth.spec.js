const { test, expect } = require('@playwright/test');

const unique = Date.now();
const username = `playwrightuser${unique}`;
const email = `playwrightuser${unique}@example.com`;
const password = 'Strong123';

test('register with valid data', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/register-page');

  await page.fill('#username', username);
  await page.fill('#email', email);
  await page.fill('#password', password);
  await page.fill('#confirmPassword', password);
  await page.click('button[type="submit"]');

  await expect(page.locator('#message')).toHaveText('Registration successful');
});

test('register with short password', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/register-page');

  await page.fill('#username', `shortpassuser${unique}`);
  await page.fill('#email', `shortpass${unique}@example.com`);
  await page.fill('#password', '123');
  await page.fill('#confirmPassword', '123');
  await page.click('button[type="submit"]');

  await expect(page.locator('#message')).toHaveText('Password must be at least 6 characters');
});

test('login with valid credentials', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/login-page');

  await page.fill('#username', username);
  await page.fill('#password', password);
  await page.click('button[type="submit"]');

  await expect(page.locator('#message')).toHaveText('Login successful');
});

test('login with wrong password', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/login-page');

  await page.fill('#username', username);
  await page.fill('#password', 'Wrong123');
  await page.click('button[type="submit"]');

  await expect(page.locator('#message')).toHaveText('Invalid username or password');
});