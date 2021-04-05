/*
Copyright (C) 2017 Semester.ly Technologies, LLC

Semester.ly is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Semester.ly is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
*/

import React from 'react';
import PropTypes from 'prop-types';
import * as SemesterlyPropTypes from '../constants/semesterlyPropTypes';
import InviteAdvisorsModalContainer from './containers/modals/invite_advisors_modal_container';
import ReactTooltip from 'react-tooltip';
import CommentSlot from './comment_slot';
import {getNextAvailableColour} from '../util';
import CommentInputContainer from './containers/comment_input_container';
import Transcript from './transcript';
import {getTranscriptCommentsBySemester} from '../constants/endpoints';


class CommentForum extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          //TODO: Set this to the semester that is selected on the LHS
          semester_name: 'Spring',
          semester_year: 2021,
          transcript: null,
          comments: null,
          //TODO: Set this to list of student's advisors from SIS
          advisors: [
            'Yair Amir',
            'Linda Moulton',
            'Steven Marra',
          ]
        };
    }

    componentDidMount() {
      fetch(getTranscriptCommentsBySemester(this.state.semester_name, this.state.semester_year))
        .then(response => response.json())
        .then(data => {
          this.setState({transcript: data.transcript});
          this.setState({comments: this.state.transcript.comments});
        });
      // TODO: Check for error response
      // TODO: Add function for fetching list of advisors from SIS data and saving their names in this.state.advisors
    }

  render() {

        const addButton = (
          <div className="cal-btn-wrapper">
            <button
              onClick={this.props.toggleInviteAdvisorsModal}
              className="save-timetable add-button"
              data-tip
              data-for="add-btn-tooltip"
            >
              <i className="fa fa-plus" />
            </button>
            <ReactTooltip
              id="add-btn-tooltip"
              class="tooltip"
              type="dark"
              place="bottom"
              effect="solid"
            >
              <span>Invite Advisors</span>
            </ReactTooltip>
          </div>
        );

        let transcript;
        if (this.state.comments != null) {
            transcript = <Transcript
                comments={this.state.comments}
            />;
        } else {
            transcript = <div className="empty-state"><h4> <p> No comments yet! </p> </h4></div>;
        }

        return (
            <div className="comment-forum no-print">
                <div className="cf-name">
                    <p style={{fontSize: "1.25em", fontWeight: "bold", marginTop: "70px" }}>
                        Comments Forum
                    </p>
                </div>
                <InviteAdvisorsModalContainer advisors={this.state.advisors}/>
                { addButton }
                <div className="as-header"></div>
                <div className="comment-forum-container">
                  { transcript }
                </div>
                <div className="as-header"></div>
                <CommentInputContainer />
            </div>
        );
    }
}

CommentForum.defaultProps = {
    invitedComments: null,
    ownedComments: null,
}


CommentForum.propTypes = {
    toggleInviteAdvisorsModal: PropTypes.func.isRequired,
    //invitedComments: PropTypes.arrayOf(SemesterlyPropTypes.userInfo.invited_transcripts).isRequired,
    //ownedComments: PropTypes.arrayOf(SemesterlyPropTypes.userInfo.owned_transcripts).isRequired,
};

export default CommentForum;
