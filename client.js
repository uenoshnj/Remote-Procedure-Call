
function connect(){

}

function inputMethod(){
    let method = prompt("メソッドを入力してください。");
    return method;
}

function inputArgs(method){
    let argStr = prompt("引数を入力してください。");
    let argArr = [];
    switch (method) {
        case 'floor':
            argArr.push(Number(argStr));
            break;
        case 'nroot':
            argArr = argStr.split(',').map(Number);
            break;
        case 'reverse':
            argArr.push(argStr);
            break;
        case 'validAnagram':
            argArr = argStr.split(',');
            break;
        case 'sort':
            argArr = argStr.split(',');
            break;
        default:
            throw new Error("有効なメソッドを入力してください。")
    }
    return argArr;
}

function argType(argArr){
    let argTypes = [];
    for (let i = 0; i < argArr.lenth; i++) {
        argTypes.push(typeof argArr[i]);
    }
    return argTypes;
}



function request(){
    method = inputMethod();
    console.log(method);
    args = inputArgs(method);
    console.log(args);
    argTypes = argType(args);
    console.log(argTypes);
}

request();