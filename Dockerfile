# Use the official Nginx image as base
FROM nginx:alpine

# Copy the static HTML file to Nginx's default public folder
COPY index.html /usr/share/nginx/html/index.html
