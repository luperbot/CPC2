(function () {
  'use strict';

  var app = angular.module('PlantsApp', []);

  app.controller('plantsSelection', ['$scope', '$http',
    function ($scope, $http) {
      // Set intial values.
      $scope.selected_plants = {};
      $scope.errors = [];
      $scope.plants_num = 0;
      $scope.plot_width_max = 11;
      $scope.plot_length_max = 11;
      $scope.plot_width = 0;
      $scope.plot_length = 0;

      var addError = function (error) {
        if ($scope.errors.indexOf(error)) {
          $scope.errors.push(error);
        }
      }

      $scope.range = function(num) {
        return Array.apply(null, Array(num)).map(function (_, i) {return i;});
      }

      // Function to check if Plot is full or not.
      $scope.plotFull = function () {
        if (! ($scope.plot_width * $scope.plot_length) ) {
          addError("Plot size not selected.");
          return true;
        }
        if ( ($scope.plot_width * $scope.plot_length) < $scope.plants_num + 1) {
          addError("Plot is full.");
          return true;
        }
        return false;
      }

      // Get list of avaliable plants.
      $http.get('plants.json').then(
        function (data) {
          // If success of getting plants information.
          for (var plant in data.data) {
            $scope.selected_plants[plant] = 0;
          }
          $scope.plants = data.data;
        },
        function (data) {
          // If failure of getting plants information.
          addError('Unable to retrieve list of plants.');
      });

      // Function to add plants from the main list.
      $scope.addPlant = function (plant) {
        if ($scope.plotFull()) {
          return false;
        }
        $scope.plants_num += 1;
        $scope.selected_plants[plant] += 1;
      }

      $scope.removePlant = function (plant) {
        $scope.plants_num -= 1;
        $scope.selected_plants[plant] -= 1;
      }

      // Function to determine current step.
      $scope.currentStep = function (step) {
        var plot_size = $scope.plot_width * $scope.plot_length;
        if (!plot_size) {
          return step === 1;
        } else if (plot_size > $scope.plants_num) {
          return step === 2;
        } else {
          return step === 3;
        }
      }

    }]);

})();

