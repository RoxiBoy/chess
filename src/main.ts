import './style.css'

const canvas = document.getElementById('board')
const ctx = canvas.getContext('2d')

const squareSize = canvas.width / 8;

const image = new Image()
image.src = '../assets/rookblack'

const svgImage = new Image();
svgImage.src = "../assets/rookblack"

const bK = '../assets/kingblack'
const bQ = '../assets/queenblack'
const bR = '../assets/rookblack'
const bB = '../assets/bishopblack'
const bN = '../assets/knightblack'
const bP = '../assets/pawnblack'

const wK = '../assets/kingwhite'
const wQ = '../assets/queenwhite'
const wR = '../assets/rookwhite'
const wB = '../assets/bishopwhite'
const wN = '../assets/knightwhite'
const wP = '../assets/pawnwhite'

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
  ctx.drawImage(image, 0, 0)
  ctx.drawImage(image, 50, 50, 200, 100);
}

drawBoard()
renderPieces()