package com.example;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Scanner;

public class MainApp {

    public static void main(String[] args) {
        // Path to your Python script and Python executable
        String pythonScriptPath = "C:\\Users\\ASUS\\IdeaProjects\\LogisticRegressionIntegration\\src\\main\\resources\\model\\model_predict.py"; // Adjust this path
        String pythonExecutable = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"; // Full path to Python executable

        // Create a Scanner object to read input from the console
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter a URL
        System.out.print("Enter the URL to check: ");
        String url = scanner.nextLine();  // Get the URL input from the user

        // Check if URL is not empty before proceeding
        if (url.trim().isEmpty()) {
            System.out.println("URL cannot be empty!");
            scanner.close();
            return;
        }

        try {
            // Build the command to run the Python script with user input (URL)
            ProcessBuilder processBuilder = new ProcessBuilder(pythonExecutable, pythonScriptPath, url);
            processBuilder.redirectErrorStream(true); // Capture errors and stdout together

            // Set the working directory for the process (ensure it’s correct)
            processBuilder.directory(new java.io.File("C:\\Users\\ASUS\\IdeaProjects\\LogisticRegressionIntegration"));

            // Start the process
            Process process = processBuilder.start();

            // Read the output from the Python script
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;

            System.out.println("URL being passed to Python script: " + url);

            // Display the output from Python script
            while ((line = reader.readLine()) != null) {
                System.out.println(line);  // Print output from Python script
            }

            // Wait for the Python script to finish and get the exit code
            int exitCode = process.waitFor();
            if (exitCode != 0) {
                System.out.println("Python script exited with error code: " + exitCode);
            } else {
                System.out.println("Python script executed successfully.");
            }

        } catch (IOException | InterruptedException e) {
            System.out.println("Error occurred while executing Python script: " + e.getMessage());
            e.printStackTrace();
        } finally {
            // Close the scanner
            scanner.close();
        }
    }
}
