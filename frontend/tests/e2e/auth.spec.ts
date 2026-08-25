import { test, expect } from '@playwright/test';

test.describe('Smart Home Service Platform Auth Flow', () => {
  test('should display homepage with services catalog and auth buttons', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveTitle(/Smart Home Service Platform/i);
    await expect(page.getByText('Book Trusted Home Services')).toBeVisible();
    await expect(page.getByText('Popular Home Services')).toBeVisible();
  });

  test('should navigate to registration page', async ({ page }) => {
    await page.goto('/');
    await page.click('text=Get Started');
    await expect(page).toHaveURL(/\/register/);
    await expect(page.getByText('Create Your Account')).toBeVisible();
  });

  test('should allow role tab switching on register page', async ({ page }) => {
    await page.goto('/register');
    await page.click('button:has-text("TECHNICIAN")');
    await expect(page.getByText('Primary Specialization')).toBeVisible();
  });
});
