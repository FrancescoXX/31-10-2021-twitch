const User = require('../models/users');

//Crud controllers

// Create new user
exports.createOne = async (req, res, next) => {
  console.log("createOne");
  try {
    const USER_MODEL = {
      username: req.body.username,
      password: req.body.password
    }
    try {
      const user = await User.create(USER_MODEL);
      return res.status(201).json(user)
    } catch (error) {
      return res.status(500).json(error)
    }
  } catch (error) {
    return res.status(400).json("BAD REQUEST", error)
  }
}