var crypto = require('crypto');
var multer = require("multer"),
    mime = require("mime"),
    main = require('../controllers/mainController.js');
storage = multer.diskStorage({
    destination: function(req, file, cb) {
        cb(null, './public/img')
    },
    filename: function(req, file, cb) {
        crypto.pseudoRandomBytes(16, function(err, raw) {
            cb(null, raw.toString('hex') + Date.now() + '.' + mime.extension(file.mimetype));
        });
    }
})
var upload = multer({ storage: storage })
module.exports = function(app) {
    app.get('/', function(req, res) {
        res.render("main")
    })
    app.post('/', upload.single('doc'), main.extractWords);
    app.post('/cloud', main.generateTags);
}
