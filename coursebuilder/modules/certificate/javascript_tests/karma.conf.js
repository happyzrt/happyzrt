module.exports = function(config) {
  config.set({
    basePath: '../../..',
    files: [
      'https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js',
      'modules/certificate/javascript_tests/*.js',
      {
        pattern: 'modules/certificate/javascript_tests/*.html',
        watched: true,
        included: false,
        served: true
      },
      'modules/certificate/course_settings.js'
    ],
    exclude: ['**/karma.conf.js'],
    frameworks: ['jasmine-jquery', 'jasmine'],
    browsers: ['PhantomJS'],
    singleRun: true
  });
};
