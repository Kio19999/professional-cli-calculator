const { test, expect } = require('@playwright/test');

test('calculation page loads', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/calculations-page');
  await expect(page.locator('h1')).toHaveText('Calculation BREAD Operations');
});

test('create calculation from frontend', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/calculations-page');

  await page.fill('#addA', '10');
  await page.fill('#addB', '5');
  await page.selectOption('#addType', 'add');
  await page.click('#addForm button[type="submit"]');

  await expect(page.locator('#message')).toHaveText('Calculation created');
  await expect(page.locator('#output')).toContainText('"result": 15');
});

test('browse calculations from frontend', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/calculations-page');

  await page.click('#loadButton');

  await expect(page.locator('#message')).toHaveText('Calculations loaded');
  await expect(page.locator('#output')).toContainText('[');
});

test('update and delete calculation from frontend', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/calculations-page');

  await page.fill('#addA', '8');
  await page.fill('#addB', '2');
  await page.selectOption('#addType', 'multiply');
  await page.click('#addForm button[type="submit"]');

  await expect(page.locator('#message')).toHaveText('Calculation created');

  const outputText = await page.locator('#output').innerText();
  const created = JSON.parse(outputText);
  const id = created.id.toString();

  await page.fill('#editId', id);
  await page.fill('#editA', '20');
  await page.fill('#editB', '4');
  await page.selectOption('#editType', 'divide');
  await page.click('#editForm button[type="submit"]');

  await expect(page.locator('#message')).toHaveText('Calculation updated');
  await expect(page.locator('#output')).toContainText('"result": 5');

  await page.fill('#deleteId', id);
  await page.click('#deleteButton');

  await expect(page.locator('#message')).toHaveText('Calculation deleted');
});

test('create power calculation from frontend', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/calculations-page');

  await page.fill('#addA', '2');
  await page.fill('#addB', '3');
  await page.selectOption('#addType', 'power');
  await page.click('#addForm button[type="submit"]');

  await expect(page.locator('#message')).toHaveText('Calculation created');
  await expect(page.locator('#output')).toContainText('"type": "power"');
  await expect(page.locator('#output')).toContainText('"result": 8');
});