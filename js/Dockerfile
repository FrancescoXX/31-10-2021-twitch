FROM node:14

WORKDIR /src

EXPOSE 3000

COPY package*.json .

RUN npm install

COPY . . 

CMD ["node","index.js"]