# Libre - a reponsive single page app template for collection management projects.

![Libre](./screen.png)

Libre is a responsive single page app template designed for developers who want to create collection management-like projects (e.g. books, music, podcasts, games, etc.). Built with tailwind.css and vanilla javascript, this template is easily customizable and has common components like profile, lists, filters and popovers which sets the ground work for your projects. Libre is made for aduki exclusively.

## Running the project locally
Make sure your local version is v6+. I currently we are using v10.8 as of March 2021.
```
npm install
```

If you want to regenerate css with your changes, run this command to generate css using tailwind config (e.g. tailwind.js)
```
$ ./node_modules/.bin/tailwind build style.css -c ./tailwind.js -o ./output.css
```

If you want to recompile the javascript, make sure browserify is installed globally then run this command to create bundle.js
```
$ npm install -g browserify
$ browserify main.js -o bundle.js
```

## Live Demo
👋 [Libre Live Demo](http://femar.great-site.net)

## Credits
- [Browserify](http://browserify.org/)
- [Anime.js](http://animejs.com/)
- [tippy.js](https://atomiks.github.io/tippyjs/)
- [Tailwind.css](https://tailwindcss.com/)
- [Shopify Polaris's Icons](https://polaris.shopify.com/)

## License
Use it freely but please do not republish, distribute or sell "as-is". [Read more about Us.]()

## Misc

Follow femar: [Website](https://www.omba.site/), [Dribbble](http://www.dribbble.com/fescii), [Github](https://github.com/fescii), [Twitter](https://twitter.com/femar_will), [Medium](https://medium.com/@)

Follow aduki, Inc : [Twitter](http://www.twitter.com/aduki_inc), [Facebook](http://www.facebook.com/pages/), [Google+](https://plus.google.com/), [GitHub](https://github.com/aduki-inc), [Pinterest](http://www.pinterest.com/)

[© aduki, Inc 2021](http://www.aduki.net)
