import { expect } from 'chai'
import userTestData from '../utils/userTestData.js'
import testData from '../utils/testData.js'
import PostModel from '../models/PostModel.js'
import SortUtils from '../utils/SortUtils.js'
import ApiUtils from '../utils/ApiUtils.js'
import JsonPlaceholderApi from '../api/JsonPlaceholderApi.js'


describe('Test API jsonplaceholder', function (){

    it('GET all posts, posts id=99, posts id=150, all users, users id=5 and POST message', async function(){
        const responseAll = await JsonPlaceholderApi.getAllPosts()
        expect(responseAll.status).to.be.equal(testData.statusCode.status200)
        const postsAll = await responseAll.json()
        expect(postsAll).to.be.an('Array')
        expect(await SortUtils.ascendingId(postsAll)).to.be.true

        const response99 = await JsonPlaceholderApi.get99Posts()
        expect(response99.status).to.be.equal(testData.statusCode.status200)
        const expectedData99 = new PostModel(testData.dataPosts99.userId, null, null, testData.dataPosts99.id)
        const posts99 = await response99.json()
        expect(posts99.userId).to.be.equal(expectedData99.userId)
        expect(posts99.id).to.be.equal(expectedData99.id)
        expect(posts99.title).to.be.exist
        expect(posts99.body).to.be.exist

        const response150 = await JsonPlaceholderApi.get150Posts()
        expect(response150.status).to.be.equal(testData.statusCode.status404)
        const posts150 = await response150.json()
        expect(posts150).to.be.empty

        const responsePost = await JsonPlaceholderApi.postRandomText(testData.randomPostData)
        expect(responsePost.status).to.be.equal(testData.statusCode.status201)
        const expectedRandomData = new PostModel(testData.randomPostData.userId, 
            testData.randomPostData.title, testData.randomPostData.body, null)
        const posts = await responsePost.json()
        expect(posts.userId).to.be.equal(expectedRandomData.userId)
        expect(posts.id).to.be.exist
        expect(posts.title).to.be.equal(expectedRandomData.title)
        expect(posts.body).to.be.equal(expectedRandomData.body)

        const responseUsers = await JsonPlaceholderApi.getUsers()
        expect(responseUsers.status).to.be.equal(testData.statusCode.status200)
        const users = await responseUsers.json()
        expect(users).to.be.an('Array')
        expect(await ApiUtils.getUserById(users, userTestData.id)).to.deep.include(userTestData)

        const responseUsers5 = await JsonPlaceholderApi.get5Users()
        expect(responseUsers5.status).to.be.equal(testData.statusCode.status200)
        const usersFive = await responseUsers5.json()
        expect(usersFive).to.deep.include(userTestData)
    })
})