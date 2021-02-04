var canvas = document.getElementById('mycanvas');
var context = canvas.getContext('2d');

// Create star a drawing function 
function drawStar(positionX, positionY, size) {
    context.beginPath();
    context.moveTo(positionX, positionY);
    context.lineTo(positionX + size, positionY);
    context.lineTo(positionX + size*0.15, positionY + size*0.5);
    context.lineTo(positionX + size*0.5, positionY - size*0.4);
    context.lineTo(positionX + size*0.85, positionY + size*0.5);
    context.strokeStyle = 'rgb(233, 159, 184)';
    context.stroke();
    context.fillStyle = 'rgb(233, 159, 184)';
    context.fill();
}

// Create "triangle" a drawing function
function drawTriangle(positionX, positionY, size) {
    context.beginPath();
    context.moveTo(positionX, positionY);
    context.lineTo(positionX - size / 2, positionY + size);
    context.lineTo(positionX + size / 2, positionY + size);
    context.lineTo(positionX, positionY);
    context.strokeStyle = 'rgba(0,0,0,.5)';
    context.fillStyle = 'rgba(255,165,0,.5)';
    context.stroke();
    context.fill();
}

// Create "Hexagon" a drawing function
function drawHexagon (positionX, positionY) {
    var width = 113;
    var height = 98;
    context.beginPath();
    context.moveTo(positionX, positionY);
    context.lineTo(positionX + width/2*0.5, positionY - height/2);
    context.lineTo(positionX + width/2*1.5, positionY - height/2);
    context.lineTo(positionX + width/2*2, positionY);
    context.lineTo(positionX + width/2*1.5, positionY + height/2);
    context.lineTo(positionX + width/2*0.5, positionY + height/2);
    context.lineTo(positionX, positionY);
    context.stroke();
}

// Create "CheckeredPattern" a drawing function
function drawCheckeredPattern(row, col) {
    var canvasWidth = canvas.width;
    var canvasHeight = canvas.height;
    for (var rowCounter = 0; rowCounter < row; rowCounter++) {
        for (var colCounter = 0; colCounter < col; colCounter++) {
            if (colCounter % 2 === rowCounter % 2) {
                context.fillStyle = 'white';
            } else {
                context.fillStyle = 'black';
            }
            context.fillRect(colCounter * canvasWidth / col, rowCounter * canvasHeight / row, canvasWidth / col, canvasHeight / row);
        }
    }
}