import LoginPage from '../../page/LoginPage.js';
import PasswordPage from '../../page/PasswordPage.js';
import FeedPage from '../../page/FeedPage.js';
import { assert } from 'chai';
import Logger from '../../utils/logUtils.js';
import VkApiUtils from '../../utils/VkApiUtils.js';
import generateMessage from '../../utils/generateMessage.js';
import MyProfilePage from '../../page/MyProfilePage.js';
import testData from '../../utils/testData.js';


describe('VK API test', function () {
    it('Sign in, add, edit and delete the post, add comment and like', async function(){
        
        Logger.infoLog('Go to homepage and enter login');
        await LoginPage.isPageOpen();
        await LoginPage.fillLoginField();
        await LoginPage.clickSignInButton();
        
        Logger.infoLog('Go to password page and enter password');
        await PasswordPage.fillPasswordField();
        await PasswordPage.clickSubmitButton();
        
        Logger.infoLog('Go to profile and post comment');
        await FeedPage.clickMyProfileButton();
        const randomText = await generateMessage();
        Logger.infoLog('Save Id new post');
        const postId = await VkApiUtils.postOnWall(randomText);
        
        Logger.infoLog('Check text and owner of the last post');
        const userIdFromLastPost = await MyProfilePage.getUserIdFromLastPost();
        const textFromLastPost = await MyProfilePage.isTextFromLastPostVisible(randomText);

        assert.equal(userIdFromLastPost, testData.userId, 'User from post is different');
        assert.isTrue(textFromLastPost, 'Message from new post is different');

        Logger.infoLog('Edit last post: add image and another text');
        const randomTextToNewComment = await generateMessage();
        const imageToEditPost = await VkApiUtils.postImageWall();
        await VkApiUtils.editPost(postId, randomTextToNewComment, imageToEditPost);
        const textFromLastPostEdit = await MyProfilePage.isTextFromLastPostVisible(randomTextToNewComment);
        assert.isTrue(textFromLastPostEdit, 'Message from post is not updated');
        const idImageLastPost = await MyProfilePage.getImageIdFromLastPost();
        assert.equal(imageToEditPost, idImageLastPost, 'Image is different');

        Logger.infoLog('Add comment and check User Id');
        const textToComment = await generateMessage();
        await VkApiUtils.addComment(postId, textToComment);
        const userIdFromLastComment = await MyProfilePage.getUserIdFromComment();
        assert.equal(testData.userId, userIdFromLastComment, 'User from comment is different');

        Logger.infoLog('Like last post and check this');
        await MyProfilePage.clickLikeButton();
        const userIdFromLike = await VkApiUtils.getLikeList(postId);
        assert.equal(testData.userId, userIdFromLike, 'User from like is different');

        Logger.infoLog('Delete the post and check that it is gone');
        await VkApiUtils.deletePost(postId);
        const textFromElementAfterDeletePost = await MyProfilePage.isPostMiss();
        assert.notEqual(textFromElementAfterDeletePost, randomText, 'Post is not deleted');
    });
});