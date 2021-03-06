var baseUrl = window.location.protocol + "//" + window.location.host
let currentPost = ""
async function emotion_post(post, type, element) {
    const formData = new FormData();
    formData.append('csrfmiddlewaretoken ', csrftoken);
    fetch(baseUrl + `/post/emotion/${post}/${type}`, {
            method: 'POST',
            body: formData
        })
        // .then(res => console.log(res))
        .catch(err => alert(err))
}

async function emotion_comment(comment, type, element) {
    const formData = new FormData();
    formData.append('csrfmiddlewaretoken ', csrftoken);
    fetch(baseUrl + `/comment/emotion/${comment}/${type}`, {

            method: 'POST',
            body: formData
        })
        // .then(res => console.log(res))
        .catch(err => console.log(err))
}


// function distribute() {
//     const data = { numberOfDistribution: 1 };

//     var url = 'http://127.0.0.1:8000/post/api/post/';
//     var data = { numberOfDistribution: 1 };
//     fetch(url, {
//         method: 'POST', // or 'PUT'
//         body: JSON.stringify(data), // data can be `string` or {object}!
//         headers: {
//             'Content-Type': 'application/json'
//         }
//     }).then(res => res.json())
//         .then(response => console.log('Success:', JSON.stringify(response)))
//         .catch(error => console.error('Error:', error));
// }
// function postCreate(e, url) {
//     var text = e.getElementsByClassName("text")
//     // var url = "{% url 'create_post' %}"
//     fetch(url, {
//         method: 'POST',
//         body: {
//             text
//         }
//     })
//         // .then(res => console.log(res))
//         .catch(err => alert(err))
//     console.log(url)

// }

function distribute(post_id) {
    const formData = new FormData();
    formData.append('csrfmiddlewaretoken ', csrftoken);
    fetch(`/post/api/distribute_post/${post_id}`, {
            method: 'POST',
            body: formData
        }).then(function() {
            let element = document.getElementById("post_" + post_id)
            let emo_distribute = element.getElementsByClassName("emo_distribute")[0]
            emo_distribute.innerText = "✅"

        })
        .catch(err => console.log(err))
    let modal = document.getElementsByClassName('modal-body')[0]
    emo_distribute = modal.getElementsByClassName("emo_distribute")[0]
    emo_distribute.innerText = "✅"

}

function commentCreate(post_id, url) {
    var comment = document.getElementById("comment_post" + post_id)
    var text = comment.value
    comment.value = ""
    const formData = new FormData();
    formData.append('text', text);
    fetch(url, {
            method: 'POST',
            body: formData
        })
        .then(res => console.log(res))
        .catch(err => alert(err))
}

function getComment(comment_id) {
    fetch('/comment/getcomment/' + comment_id)
        .then(res => res.json())
        .then(data => insertComment(data))
        .catch(err => console.log(err))

}

function insertComment(comment) {
    var div = document.createElement('div');

    if (comment.post_id != currentPost) {
        return
    }
    let modal = document.getElementsByClassName('modal-body')[0]
    var commentArea = modal.getElementsByClassName('comment_area')[0]
    var html = `
    <div class="card m-1" id="comment_${comment.id}">
        <div class="card-body">
            <h6>(${comment.commentBy})  ${comment.text}</h6>
            <div class="btn-group mr-2" role="group" aria-label="First group">
                <button type="submit" class="btn btn-secondary"
                    onclick="emotion_comment(${comment.id}, 1, this)">👍<span
                        class="like">${comment.like}</span></button>
                <button type="submit" class="btn btn-secondary"
                    onclick="emotion_comment(${comment.id}, 2, this)">😂<span
                        class="haha">${comment.haha}</span></button>
                <button type="submit" class="btn btn-secondary"
                    onclick="emotion_comment(${comment.id}, 3, this)">😠<span
                        class="angry">${comment.angry}</span></button>
                <button type="submit" class="btn btn-secondary"
                    onclick="emotion_comment(${comment.id}, 4, this)">😭<span
                        class="sad">${comment.sad}</span></button>
            </div>
        </div>
    </div>`
    div.innerHTML = html

    commentArea.appendChild(div)


}


function socketOnMessage(e) {
    var data = JSON.parse(e.data).message;
    if (data.addComment) {
        getComment(data.addComment)
        return
    }
    if (data.comment) {
        var element = document.getElementById("comment_" + data.comment)
    } else {
        var element = document.getElementById("post_" + data.post)
    }
    let observers = ['distribute', 'like', 'haha', 'angry', 'sad']
    for (let k = 0; k < observers.length; k++) {
        if (data[observers[k]]) {
            let component = element.getElementsByClassName(observers[k])[0]
            component.innerText = data[observers[k]]
            if (!data.comment) {
                let modal = document.getElementsByClassName('modal-body')[0]
                component = modal.getElementsByClassName(observers[k])[0]
                component.innerText = data[observers[k]]
            }

        }
    }

};

function getDetailPost(post_id) {
    fetch(`/post/api/get_detail_post/${post_id}`)
        .then(res => res.text())
        .then(function(html) {
            document.getElementById('viewDetailPost').innerHTML = html
            currentPost = post_id
        })
        .catch(err => {
            console.log("Error getPost")
        })
}

function edit_post(event, post_id) {
    text = document.getElementById(`text_post_${post_id}`);
    input = document.createElement('textarea')
    input.setAttribute('class', `form-control mb-2`)
    input.setAttribute('id', `text_post_${post_id}`)
    input.type = 'text'
    input.value = text.innerText
    text.parentNode.insertBefore(input, text);
    text.remove()
    event.innerText = '☑️ Finish'
    event.setAttribute('onclick', `updatePost(this, ${post_id})`)
}

function updatePost(event, post_id) {
    input = document.getElementById(`text_post_${post_id}`);
    const formData = new FormData();
    formData.append('csrfmiddlewaretoken', csrftoken);
    formData.append('text', input.value);
    formData.append('id', post_id);
    fetch('/post/api/edit_post/', {
            method: 'POST',
            body: formData
        })
        .then(res => {
            text = document.createElement('H6')
            text.setAttribute('class', 'card-text')
            text.setAttribute('id', `text_post_${post_id}`)
            text.innerText = input.value
            input.parentNode.insertBefore(text, input);
            input.remove()
            event.innerText = '✏️ Edit'
            event.setAttribute('onclick', `edit_post(this, ${post_id})`)
        })

    .catch(err => console.log(err))

    //input = document.createElement('INPUT')
    // input.setAttribute('class', 'form-control mb-2')
    // input.type = 'text'
    // input.value = text.innerText
    // text.parentNode.insertBefore(input, text.nextSibling);
    // text.remove()
    // event.innerText = '☑️ Finish'
    // event.setAttribute('onclick', `updatePost(${post_id})`)
}


function connectPost(post_id) {
    var chatSocket = new WebSocket(
        'ws://' + window.location.host +
        '/ws/post/post' + `${post_id}` + '/');
    chatSocket.onmessage = socketOnMessage
    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };
}

function score(user_id) {
    const formData = new FormData();
    formData.append('csrfmiddlewaretoken ', csrftoken);
    console.log(csrftoken)
    console.log('Score เข้านะจ๊ะ')
    fetch(`/user/score/${user_id}/`, {
            method: 'POST',
            body: formData
        })
        .then(alert("ให้คะแนนแล้วจ้าา"))
        .catch(err => console.log(err))
}