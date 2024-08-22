const net = require('net');

const server_address = './server_socket_file';
const client = new net.Socket(server_address);

// リクエスト用のオブジェクト
const request = {
    method: '',
    params: [],
    id: 0
}

function handleInput(params) {
    params = params.replaceAll(' ', '');
    if (params.indexOf(',') !== -1) {
        if(isFinite(params.split(',')[0])) {
            return params.split(',').map(Number);
        } else {
            return params.split(',');
        }
    } else if(isFinite(params)) {
        return Number(params);
    } else {
        return params;
    }
}

// ユーザの入力情報取得
function readUserInput(question) {
    const readline = require('readline');

    const { stdin: input, stdout: output, exit } = require('process');

    const rl = readline.createInterface({ input, output });

    return new Promise((resolve, reject) => {
        rl.question(question, (answer) => {
            resolve(handleInput(answer));
            rl.close();
        })
    });
}

(async function main() {
    request.method = await readUserInput('Enter the method: ');
    request.params = await readUserInput('Enter the params: ');
    request.id++;
    const jsondata = JSON.stringify(request);

    // サーバへ接続
    client.connect(server_address, () => {
        console.log('Connected to server');

        // サーバにデータを送信
        client.write(jsondata);
        console.log(`send data`, jsondata, ` to ${server_address}`);

        console.log(`
-----------------------------------
wait a minute...
-----------------------------------
        `);
    });


    // サーバからデータを受信
    client.on('data', (data) => {
        const response = JSON.parse(data);

        if (response.error) {
            console.error('Error: ', response.error);
        } else {
            console.log('Received data')
            console.log(response);
        }
    });

    // 接続を閉じる
    client.on('close', () => {
        console.log('Connection closed.')
    });
    return false;
})();
