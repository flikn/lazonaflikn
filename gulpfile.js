var basePaths = {
  src: "landing/frontdev/",
  dest: "landing/static/",
  bower: "bower_components/"
};

var paths = {
  fonts: {
    src: basePaths.src + "fonts/",
    dest: basePaths.dest + "fonts/"
  },
  img: {
    src: basePaths.src + "img/",
    dest: basePaths.dest + "img/"
  },
  sprites: {
    src: basePaths.src + "sprites/*"
  },
  scripts: {
    src: basePaths.src + "js/",
    dest: basePaths.dest + "js/"
  },
  styles: {
    src: basePaths.src + "scss/",
    dest: basePaths.dest + "css/"
  },
};

var appFiles = {
  fonts: paths.fonts.src + "**",
  img: paths.img.src + "**",
  sprites: paths.sprites.src + "**",
  scripts: paths.scripts.src + "**",
  styles: paths.styles.src + "**/*.scss",
};

var main_styles = {
  styles: [
    basePaths.bower + "normalize.css/normalize.css",
    paths.styles.src + "main.scss"
  ]
};

/*Let the magic begin*/

var gulp = require("gulp"),
  sass = require("gulp-sass"),
  rename = require("gulp-rename");
  

gulp.task("sass", function() {
  return gulp.src(main_styles.styles)
    .pipe(sass({
      outputStyle: "compressed",
      sourceComments: "map",
      sourceMap: "sass"
    }))
    .pipe(rename({
      suffix: ".min"
    }))
    .pipe(gulp.dest(paths.styles.dest));
});

gulp.task("copy", function() {
  gulp.src(paths.fonts.src + "**")
    .pipe(gulp.dest(paths.fonts.dest));
  gulp.src(paths.img.src + "**")
    .pipe(gulp.dest(paths.img.dest));
  gulp.src(paths.scripts.src + "**")
    .pipe(gulp.dest(paths.scripts.dest));
});

gulp.task("watch", function() {
  gulp.watch(appFiles.styles, ["sass"]);
  gulp.watch(appFiles.img, ["copy"]);
  gulp.watch(appFiles.fonts, ["copy"]);
  gulp.watch(appFiles.scripts, ["copy"]);
});

gulp.task("default", ["sass", "copy"]);
