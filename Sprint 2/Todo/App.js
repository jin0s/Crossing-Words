$(function () {
     var model = new TaskModel(),
         view = new TaskView(model),
         controller = new TaskController(model, view);
 });
