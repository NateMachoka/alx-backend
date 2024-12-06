const express = require("express");
const redis = require("redis");
const { promisify } = require("util");

const app = express();
const PORT = 1245;

const listProducts = [
  { itemId: 1, itemName: "Suitcase 250", price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: "Suitcase 450", price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: "Suitcase 650", price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: "Suitcase 1050", price: 550, initialAvailableQuantity: 5 },
];

const client = redis.createClient();
const reserveStockById = (itemId, stock) => client.set(`item.${itemId}`, stock);
const getCurrentReservedStockById = promisify(client.get).bind(client);

const getItemById = (id) => listProducts.find((item) => item.itemId === id);

app.get("/list_products", (req, res) => {
  res.json(listProducts);
});

app.get("/list_products/:itemId", async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: "Product not found" });
  }

  const reservedStock = await getCurrentReservedStockById(itemId) || 0;
  const currentQuantity = item.initialAvailableQuantity - reservedStock;

  res.json({ ...item, currentQuantity });
});

app.get("/reserve_product/:itemId", async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: "Product not found" });
  }

  const reservedStock = parseInt(await getCurrentReservedStockById(itemId) || 0, 10);
  const currentQuantity = item.initialAvailableQuantity - reservedStock;

  if (currentQuantity <= 0) {
    return res.json({ status: "Not enough stock available", itemId });
  }

  reserveStockById(itemId, reservedStock + 1);
  res.json({ status: "Reservation confirmed", itemId });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
