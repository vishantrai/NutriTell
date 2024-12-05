// Nutritional data simulation
const nutritionDatabase = {
    rice: { calories: 130, protein: 2.7, fat: 0.3, carbs: 28 },
    banana: { calories: 89, protein: 1.1, fat: 0.3, carbs: 23 },
    "chhole bhature": { calories: 427, protein: 12, fat: 22, carbs: 43 },
    "aaloo paratha": { calories: 210, protein: 4.5, fat: 7, carbs: 32 },
    "chicken curry": { calories: 180, protein: 15, fat: 11, carbs: 5 },
    biryani: { calories: 290, protein: 9, fat: 10, carbs: 39 },
    "puri sabji": { calories: 280, protein: 5, fat: 12, carbs: 38 },
    dosa: { calories: 133, protein: 3, fat: 3, carbs: 22 },
    idli: { calories: 58, protein: 2, fat: 0.4, carbs: 12 },
    "paneer butter masala": { calories: 320, protein: 10, fat: 26, carbs: 8 },
    "rajma chawal": { calories: 210, protein: 7, fat: 5, carbs: 32 },
    "dal tadka": { calories: 120, protein: 5, fat: 3, carbs: 15 },
    samosa: { calories: 260, protein: 4, fat: 12, carbs: 33 },
    "pav bhaji": { calories: 240, protein: 5, fat: 10, carbs: 30 },
    "masala dosa": { calories: 168, protein: 4, fat: 6, carbs: 24 },
    "roti sabji": { calories: 150, protein: 3, fat: 5, carbs: 22 },
    "fish curry": { calories: 150, protein: 18, fat: 6, carbs: 2 },
    "keema naan": { calories: 320, protein: 12, fat: 10, carbs: 42 },
    "palak paneer": { calories: 230, protein: 10, fat: 16, carbs: 8 },
    "veg pulao": { calories: 200, protein: 5, fat: 5, carbs: 32 },
    kheer: { calories: 150, protein: 4, fat: 5, carbs: 23 },
    "gajar halwa": { calories: 180, protein: 4, fat: 8, carbs: 25 },
  };
  
  // Function to fetch and calculate nutritional info
  function getNutritionalInfo(foodName, amount) {
    const normalizedFoodName = foodName.toLowerCase();
    const food = nutritionDatabase[normalizedFoodName];
    if (!food) {
      return `No data available for "${foodName}". Please try another food.`;
    }
  
    const multiplier = amount / 100; // Nutritional values are per 100g
    return `
      <ul>
        <li><strong>Calories:</strong> ${(food.calories * multiplier).toFixed(2)} kcal</li>
        <li><strong>Protein:</strong> ${(food.protein * multiplier).toFixed(2)} g</li>
        <li><strong>Fat:</strong> ${(food.fat * multiplier).toFixed(2)} g</li>
        <li><strong>Carbohydrates:</strong> ${(food.carbs * multiplier).toFixed(2)} g</li>
      </ul>
    `;
  }
  
  // Form submission handler
  document.getElementById("nutritionForm").addEventListener("submit", function (event) {
    event.preventDefault();
  
    const foodName = document.getElementById("food").value.trim();
    const amount = parseFloat(document.getElementById("amount").value.trim());
  
    if (!foodName || isNaN(amount) || amount <= 0) {
      document.getElementById("output").innerHTML = "<p>Please enter valid food name and amount.</p>";
      return;
    }
  
    const result = getNutritionalInfo(foodName, amount);
    document.getElementById("output").innerHTML = result;
  });
  