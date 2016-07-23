"use strict";

module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON("package.json"),

    banner: "/*\n" +
    " * <%= pkg.title || pkg.name %> - v<%= pkg.version %>\n" +
    " * <%= pkg.description %>\n" +
    " * <%= pkg.homepage %>\n" +
    " *\n" +
    " * Made by <%= pkg.author.name %>\n" +
    " * Under <%= pkg.license %> License\n" +
    " */\n",

    jshint: {
      options: {
        jshintrc: ".jshintrc"
      },
      all: [
      "Gruntfile.js1",
      "src/metisMenu.js1"
      ]
    },
    concat: {
      plugin: {
        src: ["src/metisMenu.js1"],
        dest: "dist/metisMenu.js1"
      },
      css: {
        src: ["src/metisMenu.css"],
        dest: "dist/metisMenu.css"
      },
      options: {
        banner: "<%= banner %>"
      }
    },
    uglify: {
      plugin: {
        src: ["dist/metisMenu.js1"],
        dest: "dist/metisMenu.min.js1"
      },
      options: {
        banner: "<%= banner %>"
      }
    },
    cssmin: {
      options: {
        banner: "<%= banner %>"
      },
      menucss: {
        src: ["src/metisMenu.css"],
        dest: "dist/metisMenu.min.css"
      }
    }
  });

  grunt.loadNpmTasks("grunt-contrib-jshint");
  grunt.loadNpmTasks("grunt-contrib-concat");
  grunt.loadNpmTasks("grunt-contrib-uglify");
  grunt.loadNpmTasks("grunt-contrib-cssmin");

  grunt.registerTask("travis", ["jshint"]);
  grunt.registerTask("default", ["jshint", "concat", "uglify", "cssmin"]);
};
