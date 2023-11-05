import './style.css'

const canvas = document.getElementById('board')! as HTMLCanvasElement
const ctx = canvas.getContext('2d')!

const squareSize = canvas.width / 8;

const bK = new Image();
bK.src = '../assets/kingblack.svg'

const bQ = new Image 
bQ.src = '../assets/queenblack.svg'

const bR = new Image();
bR.src = '../assets/rookblack.svg';

const bB = new Image();
bB.src = '../assets/bishopblack.svg';

const bN = new Image();
bN.src = '../assets/knightblack.svg';

const bP = new Image();
bP.src = '../assets/pawnblack.svg';

const wK = new Image();
wK.src = '../assets/kingwhite.svg';

const wQ = new Image();
wQ.src = '../assets/queenwhite.svg';

const wR = new Image();
wR.src = '../assets/rookwhite.svg';

const wB = new Image();
wB.src = '../assets/bishopwhite.svg';

const wN = new Image();
wN.src = '../assets/knightwhite.svg';

const wP = new Image();
wP.src = '../assets/pawnwhite.svg';

// Define the chess pieces with their properties
const piecesPos = [
  // Black pieces
  { name: 'bRook1', image: bR, x: 0, y: 0, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'bKnight1', image: bN, x: squareSize, y: 0, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'bBishop1', image: bB, x: 2 * squareSize, y: 0, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'bQueen', image: bQ, x: 3 * squareSize, y: 0, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'bKing', image: bK, x: 4 * squareSize, y: 0, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'bBishop2', image: bB, x: 5 * squareSize, y: 0, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'bKnight2', image: bN, x: 6 * squareSize, y: 0, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'bRook2', image: bR, x: 7 * squareSize, y: 0, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'bPawn1', image: bP, x: 0, y: squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'bPawn2', image: bP, x: squareSize, y: squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'bPawn3', image: bP, x: 2 * squareSize, y: squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'bPawn4', image: bP, x: 3 * squareSize, y: squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'bPawn5', image: bP, x: 4 * squareSize, y: squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'bPawn6', image: bP, x: 5 * squareSize, y: squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'bPawn7', image: bP, x: 6 * squareSize, y: squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'bPawn8', image: bP, x: 7 * squareSize, y: squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  // White pieces
  { name: 'wRook1', image: wR, x: 0, y: 7 * squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'wKnight1', image: wN, x: squareSize, y: 7 * squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'wBishop1', image: wB, x: 2 * squareSize, y: 7 * squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'wQueen', image: wQ, x: 3 * squareSize, y: 7 * squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'wKing', image: wK, x: 4 * squareSize, y: 7 * squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'wBishop2', image: wB, x: 5 * squareSize, y: 7 * squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'wKnight2', image: wN, x: 6 * squareSize, y: 7 * squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'wRook2', image: wR, x: 7 * squareSize, y: 7 * squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'wPawn1', image: wP, x: 0, y: 6 * squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'wPawn2', image: wP, x: squareSize, y: 6 * squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0},
  { name: 'wPawn3', image: wP, x: 2 * squareSize, y: 6 * squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'wPawn4', image: wP, x: 3 * squareSize, y: 6 * squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'wPawn5', image: wP, x: 4 * squareSize, y: 6 * squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'wPawn6', image: wP, x: 5 * squareSize, y: 6 * squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'wPawn7', image: wP, x: 6 * squareSize, y: 6 * squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 },
  { name: 'wPawn8', image: wP, x: 7 * squareSize, y: 6 * squareSize, isDragging: false, dragOffsetX: 0, dragOffsetY: 0 }
];
const drawBoard = () => {
  for (let row = 0; row < 8; row++) {
    for (let col = 0; col < 8; col++) {
        
        if ((row + col) % 2 === 0) {
            ctx.fillStyle = 'white';
        } else {
            ctx.fillStyle = '#df5413';
        }
        ctx.fillRect(col * squareSize, row * squareSize, squareSize, squareSize);
    }
  }
}

const renderPieces = () => {
  for (const piece of piecesPos) {
      // Draw the piece at its initial position
      ctx.drawImage(piece.image, piece.x, piece.y, squareSize, squareSize);
    
  }
};

// Define the chess pieces with their properties


canvas.addEventListener('mousedown', (e) => {
  const mouseX = e.clientX - canvas.getBoundingClientRect().left
  const mouseY = e.clientY - canvas.getBoundingClientRect().top

  for(const piece of piecesPos){
    if(
      mouseX >= piece.x &&
      mouseX <= piece.x + squareSize &&
      mouseY >= piece.y &&
      mouseY <= piece.y + squareSize
    ){
      piece.isDragging = true;
      piece.dragOffsetX = mouseX - piece.x
      piece.dragOffsetY = mouseY - piece.y
      break
    }

  }
})

canvas.addEventListener('mousemove', (e) => {
  for(const piece of piecesPos) {
    if(piece.isDragging){
      const mouseX = e.clientX - canvas.getBoundingClientRect().left
      const mouseY = e.clientY - canvas.getBoundingClientRect().top

      piece.x = mouseX - piece.dragOffsetX
      piece.y = mouseY - piece.dragOffsetY

      drawBoard()
      renderPieces()
    }
  }
})

canvas.addEventListener('mouseup', (e) => {
  for(const piece of piecesPos) {
    if(piece.isDragging){
      const mouseX = e.clientX - canvas.getBoundingClientRect().left
      const mouseY = e.clientY - canvas.getBoundingClientRect().top

      piece.x = Math.floor(mouseX/75) * squareSize
      piece.y = Math.floor(mouseY/75) * squareSize

      piece.isDragging = false

      console.log(mouseX, mouseY)

      drawBoard()
      renderPieces()
    }
  }
})

window.addEventListener('load', () => {
  drawBoard()
  renderPieces()
})

