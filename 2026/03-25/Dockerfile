FROM node:alpine
WORKDIR /app

COPY package.json ./
RUN npm install

COPY . .
EXPOSE 5171
CMD npm run dev -- --host 0.0.0.0
