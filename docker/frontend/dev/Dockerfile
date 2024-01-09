# Use a Node.js base image so we don't have to install a bunch of extra things
FROM node:18-alpine as development

WORKDIR /app/theme

# Copy the package.json and package-lock.json files over
COPY theme/package*.json ./

# Now we run yarn install, which includes dev dependencies
RUN yarn install

# Copy the rest of our source code over to the image
# COPY ./src ./src

# Run our start:dev command, which uses nodemon to watch for changes
CMD [ "yarn", "run", "theme:dev" ]

# "Builder" stage extends from the "development" stage but does an NPM clean install with only production dependencies 
# FROM development as builder
# WORKDIR /usr/src/app
# RUN rm -rf node_modules
# RUN npm ci --only=production
# CMD [ "yarn", "run", "theme:build" ]
 
# Final stage uses a very small image and copies the built assets across from the "builder" stage
# FROM alpine:latest as production
# RUN apk --no-cache add nodejs ca-certificates
# WORKDIR /root/
# COPY --from=builder /usr/src/app ./
# CMD [ "node", "src/index.js" ]
