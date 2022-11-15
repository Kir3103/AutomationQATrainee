export default class PostModel {

    constructor(userId, title, body, id) {
        this._userId = userId
        this._title = title
        this._body = body
        this._id = id
    }
    get userId() {
        return this._userId
    }
    set userId(userId) {
        this._userId = userId
    }

    get title() {
        return this._title
    }
    set title(title) {
        this._title = title
    }

    get body() {
        return this._body
    }
    set body(body) {
        this._body = body
    }

    get id() {
        return this._id
    }
    set id(id) {
        this._id = id
    }
}