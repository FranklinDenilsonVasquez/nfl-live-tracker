// server/index.js
const express = require("express");
const mysql = require("mysql2");

const app = express();
const port = 5000;

// Create a MySQL connection
const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "your_password",
  database: "nfl_stats",
});

// Connect to MySQL
db.connect((err) => {
  if (err) throw err;
  console.log("Connected to MySQL!");
});

// Sample route
app.get("/", (req, res) => {
  res.send("NFL Stats API");
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
