**URL Shortener API**

###### Features:

- Shorten any long URL
- Redirect via code
- Track visit count
- Support JWT-based users: admin can see analytics, user can only shorten link

###### API Endpoints:

- POST /register (create user)
- POST /login (returns JWT)
- POST /shorten (shorten URL (auth)
- GET /{code} (redirect to original URL)
- GET /analytics (only admin can access)

URL Shortner API Document link:- [click](https://drive.google.com/file/d/16iLKeiWJE36rWBp-meLfWbCKl_L66PkM/view?usp=drive_link)
