const exec = require('child_process').exec;


exports.extractWords = function(req, res) {
    console.dir(req.file);
    console.log("I am here!")
        /*require("fs").writeFileSync("/python/textForms1/0000.txt", text)*/
    exec('python python/main.py ' + req.file.filename, (error, stdout, stderr) => {
        if (error) {
            console.log(`stdout: ${stdout}`);
            console.error(`exec error: ${error}`);
            return res.render("main", { "error": error });
        }
        console.log(`stdout: ${stdout}`);
        console.log(`stderr: ${stderr}`);
        return res.render("main", { words: "Not trained/compatibility issue", filename: "img/" + req.file.filename, beautified: "img/beautified_" + req.file.filename });
    });
}

exports.generateTags = function(req, res) {
    console.dir(req.body.sel1)
    exec('python ./python/tfidfCloud.py ' + req.body.sel1, (error, stdout, stderr) => {
        if (error) {
            console.log(`stdout: ${stdout}`);
            console.error(`exec error: ${error}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
        console.log(`stderr: ${stderr}`);
        return res.redirect("/");
    });
}
