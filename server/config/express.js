var express = require('express'),
	bodyParser = require('body-parser'),
	ejs = require('ejs');

module.exports = function(app, config) {
	app.set('views', config.rootPath + '/server/views');
	app.set('view engine', 'ejs');
	app.use(bodyParser.urlencoded({
		extended: true
	}));
	app.use(bodyParser.json());
	app.use(express.static('public'))
}
