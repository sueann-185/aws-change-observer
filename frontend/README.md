# Frontend Testing

## Purpose

This folder (`frontend/`) is intended solely for testing the functionality of the backend services. It contains front-end code and configurations that interact with the backend to simulate and verify backend behavior.

### Key Points:
- The frontend code here is **not** intended for production use.
- It is used to test backend services, including API Gateway and Lambda functions.
- The primary purpose is to verify API responses and ensure backend services are functioning as expected.

### How to Use

1. **Run Frontend with Live Server**:
   - This frontend can be tested using the **Live Server** extension in **Visual Studio Code**.
   - To start, open the `frontend/` folder in **VS Code**, right-click on `index.html`, and select **Open with Live Server**.
   - This will launch the frontend locally in your browser.

2. **Configure Backend URLs**: 
   - Ensure that the correct backend API URLs (e.g., API Gateway URLs) are used when testing backend functionality.

3. **Make Test Calls**: 
   - Use the UI or JavaScript `fetch()` in the frontend to make API calls and observe responses from the backend.

### Notes
- This folder is excluded from production deployments.
- The testing setup may evolve as the backend services are updated or extended.
