const express = require('express');
const sequelize = require('./util/database');
const User = require('./models/users');

const app = express()
app.use(express.json());


app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST,PUT,DELETE');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  next();
})

app.get('/', (req, res) => {
  res.send('Halloween World!')
})

app.use('/users', require('./routes/users'));


// app.listen(process.env.EXTERNAL_PORT, () => {
//   console.log(`Example app listening at http://localhost:${process.env.EXTERNAL_PORT}`)
// })

(async () => {
  try {
    console.log(process.env);
    await sequelize.sync(
      { force: false }
    );
    app.listen(process.env.EXTERNAL_PORT);
    console.log("Js app listening on port", process.env.EXTERNAL_PORT);
  } catch (error) {
   console.log(error); 
  }
})();