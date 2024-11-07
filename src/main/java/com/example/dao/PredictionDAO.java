package com.example.dao;

import com.example.util.DBConnection;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class PredictionDAO {
    public void savePrediction(String inputData, String predictionResult) {
        String query = "INSERT INTO predictions (input_data, prediction_result) VALUES (?, ?)";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(query)) {
            pstmt.setString(1, inputData);
            pstmt.setString(2, predictionResult);
            pstmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
