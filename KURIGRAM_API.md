# Kurigram: высокоуровневые методы Client

Снимок установленного Kurigram 2.2.26, 2026-09-14. Всего публичных callable-методов: 425.
Сигнатуры и краткие описания извлечены из установленной библиотеки; self — объект Client, не MCP-аргумент.
После обновления библиотеки уточняй актуальную сигнатуру через client_describe.

## Как выбирать метод

Сначала ищи здесь high-level метод. Затем client_describe(method) и client_call(method, params).
Raw API нужен только если high-level метод не покрывает задачу.
Не загружай весь справочник в контекст: ищи имя или раздел через поиск по файлу.

Для стикерпака используй get_stickers(short_name), затем send_sticker(chat_id, sticker=file_id)
с file_id выбранного стикера из ответа. Для ссылки t.me/addstickers/NAME short_name = NAME.
Не собирай file_id вручную и не скачивай стикер, если уже получен file_id.
При отсутствии подходящего метода сначала проверь client_search("sticker").

client_call возвращает максимум 100 элементов генератора; limit=0 не означает полный экспорт.
Статус ниже отражает ограничения текущего MCP gateway, а не наличие метода в библиотеке.

## Указатель

- [accept_terms_of_service](#accept_terms_of_service)
- [add_chat_members](#add_chat_members)
- [add_checklist_tasks](#add_checklist_tasks)
- [add_collection_gifts](#add_collection_gifts)
- [add_contact](#add_contact)
- [add_handler](#add_handler)
- [add_poll_option](#add_poll_option)
- [add_profile_audio](#add_profile_audio)
- [add_to_gifs](#add_to_gifs)
- [answer_callback_query](#answer_callback_query)
- [answer_chat_join_request_query](#answer_chat_join_request_query)
- [answer_guest_query](#answer_guest_query)
- [answer_inline_query](#answer_inline_query)
- [answer_pre_checkout_query](#answer_pre_checkout_query)
- [answer_shipping_query](#answer_shipping_query)
- [answer_web_app_query](#answer_web_app_query)
- [apply_boost](#apply_boost)
- [apply_gift_code](#apply_gift_code)
- [approve_all_chat_join_requests](#approve_all_chat_join_requests)
- [approve_chat_join_request](#approve_chat_join_request)
- [approve_suggested_post](#approve_suggested_post)
- [archive_chats](#archive_chats)
- [authorize](#authorize)
- [authorize_qr](#authorize_qr)
- [ban_chat_member](#ban_chat_member)
- [block_user](#block_user)
- [buy_gift_upgrade](#buy_gift_upgrade)
- [can_post_stories](#can_post_stories)
- [change_cloud_password](#change_cloud_password)
- [change_phone_number](#change_phone_number)
- [check_bot_username](#check_bot_username)
- [check_chat_folder_invite_link](#check_chat_folder_invite_link)
- [check_gift_code](#check_gift_code)
- [check_password](#check_password)
- [check_username](#check_username)
- [close_forum_topic](#close_forum_topic)
- [compose_text_with_ai](#compose_text_with_ai)
- [connect](#connect)
- [convert_gift_to_stars](#convert_gift_to_stars)
- [copy_media_group](#copy_media_group)
- [copy_message](#copy_message)
- [copy_story](#copy_story)
- [craft_gift](#craft_gift)
- [create_bot](#create_bot)
- [create_channel](#create_channel)
- [create_chat_invite_link](#create_chat_invite_link)
- [create_folder](#create_folder)
- [create_folder_invite_link](#create_folder_invite_link)
- [create_forum_topic](#create_forum_topic)
- [create_gift_collection](#create_gift_collection)
- [create_group](#create_group)
- [create_invoice_link](#create_invoice_link)
- [create_supergroup](#create_supergroup)
- [decline_all_chat_join_requests](#decline_all_chat_join_requests)
- [decline_chat_join_request](#decline_chat_join_request)
- [decline_suggested_post](#decline_suggested_post)
- [delete_all_message_reactions](#delete_all_message_reactions)
- [delete_bot_commands](#delete_bot_commands)
- [delete_business_messages](#delete_business_messages)
- [delete_channel](#delete_channel)
- [delete_chat_admin_invite_links](#delete_chat_admin_invite_links)
- [delete_chat_history](#delete_chat_history)
- [delete_chat_invite_link](#delete_chat_invite_link)
- [delete_chat_photo](#delete_chat_photo)
- [delete_contacts](#delete_contacts)
- [delete_direct_messages_chat_topic_history](#delete_direct_messages_chat_topic_history)
- [delete_ephemeral_message](#delete_ephemeral_message)
- [delete_folder](#delete_folder)
- [delete_folder_invite_link](#delete_folder_invite_link)
- [delete_forum_topic](#delete_forum_topic)
- [delete_gift_collection](#delete_gift_collection)
- [delete_message_reaction](#delete_message_reaction)
- [delete_messages](#delete_messages)
- [delete_poll_option](#delete_poll_option)
- [delete_profile_photos](#delete_profile_photos)
- [delete_stories](#delete_stories)
- [delete_supergroup](#delete_supergroup)
- [delete_user_history](#delete_user_history)
- [disconnect](#disconnect)
- [download_media](#download_media)
- [drop_gift_original_details](#drop_gift_original_details)
- [edit_chat_invite_link](#edit_chat_invite_link)
- [edit_ephemeral_message_caption](#edit_ephemeral_message_caption)
- [edit_ephemeral_message_media](#edit_ephemeral_message_media)
- [edit_ephemeral_message_reply_markup](#edit_ephemeral_message_reply_markup)
- [edit_ephemeral_message_text](#edit_ephemeral_message_text)
- [edit_folder](#edit_folder)
- [edit_forum_topic](#edit_forum_topic)
- [edit_inline_caption](#edit_inline_caption)
- [edit_inline_media](#edit_inline_media)
- [edit_inline_reply_markup](#edit_inline_reply_markup)
- [edit_inline_text](#edit_inline_text)
- [edit_message_caption](#edit_message_caption)
- [edit_message_checklist](#edit_message_checklist)
- [edit_message_media](#edit_message_media)
- [edit_message_reply_markup](#edit_message_reply_markup)
- [edit_message_text](#edit_message_text)
- [edit_star_subscription](#edit_star_subscription)
- [edit_story_caption](#edit_story_caption)
- [edit_story_media](#edit_story_media)
- [edit_story_privacy](#edit_story_privacy)
- [edit_user_star_subscription](#edit_user_star_subscription)
- [enable_cloud_password](#enable_cloud_password)
- [enable_stealth_mode](#enable_stealth_mode)
- [export_chat_invite_link](#export_chat_invite_link)
- [export_session_string](#export_session_string)
- [fetch_peers](#fetch_peers)
- [fix_text_with_ai](#fix_text_with_ai)
- [forward_media_group](#forward_media_group)
- [forward_messages](#forward_messages)
- [forward_story](#forward_story)
- [get_account_ttl](#get_account_ttl)
- [get_active_sessions](#get_active_sessions)
- [get_all_stories](#get_all_stories)
- [get_archived_stories](#get_archived_stories)
- [get_available_effects](#get_available_effects)
- [get_available_gifts](#get_available_gifts)
- [get_blocked_message_senders](#get_blocked_message_senders)
- [get_boosts](#get_boosts)
- [get_boosts_status](#get_boosts_status)
- [get_bot_commands](#get_bot_commands)
- [get_bot_default_privileges](#get_bot_default_privileges)
- [get_bot_info_description](#get_bot_info_description)
- [get_bot_info_short_description](#get_bot_info_short_description)
- [get_bot_name](#get_bot_name)
- [get_business_account_gifts](#get_business_account_gifts)
- [get_business_account_star_balance](#get_business_account_star_balance)
- [get_business_connection](#get_business_connection)
- [get_call_members](#get_call_members)
- [get_chat](#get_chat)
- [get_chat_admin_invite_links](#get_chat_admin_invite_links)
- [get_chat_admin_invite_links_count](#get_chat_admin_invite_links_count)
- [get_chat_admins_with_invite_links](#get_chat_admins_with_invite_links)
- [get_chat_audios](#get_chat_audios)
- [get_chat_audios_count](#get_chat_audios_count)
- [get_chat_event_log](#get_chat_event_log)
- [get_chat_gifts](#get_chat_gifts)
- [get_chat_gifts_count](#get_chat_gifts_count)
- [get_chat_history](#get_chat_history)
- [get_chat_history_count](#get_chat_history_count)
- [get_chat_invite_link](#get_chat_invite_link)
- [get_chat_invite_link_joiners](#get_chat_invite_link_joiners)
- [get_chat_invite_link_joiners_count](#get_chat_invite_link_joiners_count)
- [get_chat_join_requests](#get_chat_join_requests)
- [get_chat_member](#get_chat_member)
- [get_chat_members](#get_chat_members)
- [get_chat_members_count](#get_chat_members_count)
- [get_chat_menu_button](#get_chat_menu_button)
- [get_chat_online_count](#get_chat_online_count)
- [get_chat_photos](#get_chat_photos)
- [get_chat_photos_count](#get_chat_photos_count)
- [get_chat_settings](#get_chat_settings)
- [get_chat_stories](#get_chat_stories)
- [get_chats_for_folder_invite_link](#get_chats_for_folder_invite_link)
- [get_common_chats](#get_common_chats)
- [get_contacts](#get_contacts)
- [get_contacts_count](#get_contacts_count)
- [get_custom_emoji_stickers](#get_custom_emoji_stickers)
- [get_dc_option](#get_dc_option)
- [get_default_emoji_statuses](#get_default_emoji_statuses)
- [get_dialogs](#get_dialogs)
- [get_dialogs_count](#get_dialogs_count)
- [get_direct_messages_chat_topic_history](#get_direct_messages_chat_topic_history)
- [get_direct_messages_topics](#get_direct_messages_topics)
- [get_direct_messages_topics_by_id](#get_direct_messages_topics_by_id)
- [get_discussion_message](#get_discussion_message)
- [get_discussion_replies](#get_discussion_replies)
- [get_discussion_replies_count](#get_discussion_replies_count)
- [get_file](#get_file)
- [get_folder_invite_links](#get_folder_invite_links)
- [get_folders](#get_folders)
- [get_forum_topics](#get_forum_topics)
- [get_forum_topics_by_id](#get_forum_topics_by_id)
- [get_game_high_scores](#get_game_high_scores)
- [get_gift_auction_state](#get_gift_auction_state)
- [get_gift_collections](#get_gift_collections)
- [get_gift_upgrade_preview](#get_gift_upgrade_preview)
- [get_gift_upgrade_variants](#get_gift_upgrade_variants)
- [get_gifts_for_crafting](#get_gifts_for_crafting)
- [get_global_privacy_settings](#get_global_privacy_settings)
- [get_inline_bot_results](#get_inline_bot_results)
- [get_main_web_app](#get_main_web_app)
- [get_managed_bot_access_settings](#get_managed_bot_access_settings)
- [get_managed_bot_token](#get_managed_bot_token)
- [get_me](#get_me)
- [get_media_group](#get_media_group)
- [get_message_split_ranges](#get_message_split_ranges)
- [get_messages](#get_messages)
- [get_owned_bots](#get_owned_bots)
- [get_password_hint](#get_password_hint)
- [get_payment_form](#get_payment_form)
- [get_personal_channels](#get_personal_channels)
- [get_pinned_stories](#get_pinned_stories)
- [get_privacy](#get_privacy)
- [get_received_gifts](#get_received_gifts)
- [get_received_gifts_count](#get_received_gifts_count)
- [get_scheduled_messages](#get_scheduled_messages)
- [get_send_as_chats](#get_send_as_chats)
- [get_session](#get_session)
- [get_similar_channels](#get_similar_channels)
- [get_stars_balance](#get_stars_balance)
- [get_stickers](#get_stickers)
- [get_stories](#get_stories)
- [get_story_views](#get_story_views)
- [get_suitable_discussion_chats](#get_suitable_discussion_chats)
- [get_ton_balance](#get_ton_balance)
- [get_top_chats](#get_top_chats)
- [get_upgraded_gift](#get_upgraded_gift)
- [get_upgraded_gift_value_info](#get_upgraded_gift_value_info)
- [get_user_personal_chat_messages](#get_user_personal_chat_messages)
- [get_users](#get_users)
- [get_web_app_link_url](#get_web_app_link_url)
- [get_web_app_url](#get_web_app_url)
- [gift_premium_with_stars](#gift_premium_with_stars)
- [guess_extension](#guess_extension)
- [guess_mime_type](#guess_mime_type)
- [handle_download](#handle_download)
- [handle_updates](#handle_updates)
- [hide_chat_stories](#hide_chat_stories)
- [hide_gift](#hide_gift)
- [import_contacts](#import_contacts)
- [increase_gift_auction_bid](#increase_gift_auction_bid)
- [initialize](#initialize)
- [invoke](#invoke)
- [join_chat](#join_chat)
- [join_folder](#join_folder)
- [leave_chat](#leave_chat)
- [leave_folder](#leave_folder)
- [load_plugins](#load_plugins)
- [load_session](#load_session)
- [log_out](#log_out)
- [mark_chat_unread](#mark_chat_unread)
- [mark_checklist_tasks_as_done](#mark_checklist_tasks_as_done)
- [on_business_connection](#on_business_connection)
- [on_business_message](#on_business_message)
- [on_callback_query](#on_callback_query)
- [on_chat_boost](#on_chat_boost)
- [on_chat_join_request](#on_chat_join_request)
- [on_chat_member_updated](#on_chat_member_updated)
- [on_chosen_inline_result](#on_chosen_inline_result)
- [on_connect](#on_connect)
- [on_deleted_business_messages](#on_deleted_business_messages)
- [on_deleted_messages](#on_deleted_messages)
- [on_disconnect](#on_disconnect)
- [on_edited_business_message](#on_edited_business_message)
- [on_edited_message](#on_edited_message)
- [on_error](#on_error)
- [on_guest_message](#on_guest_message)
- [on_inline_query](#on_inline_query)
- [on_managed_bot](#on_managed_bot)
- [on_message](#on_message)
- [on_message_reaction](#on_message_reaction)
- [on_message_reaction_count](#on_message_reaction_count)
- [on_poll](#on_poll)
- [on_pre_checkout_query](#on_pre_checkout_query)
- [on_purchased_paid_media](#on_purchased_paid_media)
- [on_raw_update](#on_raw_update)
- [on_shipping_query](#on_shipping_query)
- [on_start](#on_start)
- [on_stop](#on_stop)
- [on_stopped_message_generation](#on_stopped_message_generation)
- [on_story](#on_story)
- [on_user_status](#on_user_status)
- [open_web_app](#open_web_app)
- [pin_chat_message](#pin_chat_message)
- [pin_chat_stories](#pin_chat_stories)
- [pin_forum_topic](#pin_forum_topic)
- [place_gift_auction_bid](#place_gift_auction_bid)
- [process_chat_has_protected_content_disable_request](#process_chat_has_protected_content_disable_request)
- [process_gift_purchase_offer](#process_gift_purchase_offer)
- [promote_chat_member](#promote_chat_member)
- [read_chat_history](#read_chat_history)
- [read_chat_stories](#read_chat_stories)
- [read_mentions](#read_mentions)
- [read_reactions](#read_reactions)
- [recover_gaps](#recover_gaps)
- [recover_password](#recover_password)
- [refund_star_payment](#refund_star_payment)
- [remove_cloud_password](#remove_cloud_password)
- [remove_collection_gifts](#remove_collection_gifts)
- [remove_handler](#remove_handler)
- [remove_profile_audio](#remove_profile_audio)
- [reorder_collection_gifts](#reorder_collection_gifts)
- [reorder_folders](#reorder_folders)
- [reorder_gift_collections](#reorder_gift_collections)
- [replace_managed_bot_token](#replace_managed_bot_token)
- [request_callback_answer](#request_callback_answer)
- [resend_code](#resend_code)
- [resend_phone_number_code](#resend_phone_number_code)
- [reset_session](#reset_session)
- [reset_sessions](#reset_sessions)
- [resolve_peer](#resolve_peer)
- [restart](#restart)
- [restrict_chat_member](#restrict_chat_member)
- [retract_vote](#retract_vote)
- [reuse_star_subscription](#reuse_star_subscription)
- [revoke_chat_invite_link](#revoke_chat_invite_link)
- [run](#run)
- [save_file](#save_file)
- [search_contacts](#search_contacts)
- [search_gifts_for_resale](#search_gifts_for_resale)
- [search_global](#search_global)
- [search_global_count](#search_global_count)
- [search_messages](#search_messages)
- [search_messages_count](#search_messages_count)
- [search_posts](#search_posts)
- [search_posts_count](#search_posts_count)
- [send_animation](#send_animation)
- [send_audio](#send_audio)
- [send_cached_media](#send_cached_media)
- [send_chat_action](#send_chat_action)
- [send_chat_join_request_web_app](#send_chat_join_request_web_app)
- [send_checklist](#send_checklist)
- [send_code](#send_code)
- [send_contact](#send_contact)
- [send_dice](#send_dice)
- [send_document](#send_document)
- [send_game](#send_game)
- [send_gift](#send_gift)
- [send_gift_purchase_offer](#send_gift_purchase_offer)
- [send_inline_bot_result](#send_inline_bot_result)
- [send_invoice](#send_invoice)
- [send_live_photo](#send_live_photo)
- [send_location](#send_location)
- [send_media_group](#send_media_group)
- [send_message](#send_message)
- [send_message_draft](#send_message_draft)
- [send_paid_media](#send_paid_media)
- [send_paid_reaction](#send_paid_reaction)
- [send_payment_form](#send_payment_form)
- [send_phone_number_code](#send_phone_number_code)
- [send_photo](#send_photo)
- [send_poll](#send_poll)
- [send_reaction](#send_reaction)
- [send_recovery_code](#send_recovery_code)
- [send_resold_gift](#send_resold_gift)
- [send_rich_message](#send_rich_message)
- [send_rich_message_draft](#send_rich_message_draft)
- [send_screenshot_notification](#send_screenshot_notification)
- [send_sticker](#send_sticker)
- [send_story](#send_story)
- [send_venue](#send_venue)
- [send_video](#send_video)
- [send_video_note](#send_video_note)
- [send_voice](#send_voice)
- [send_web_page](#send_web_page)
- [set_account_ttl](#set_account_ttl)
- [set_administrator_title](#set_administrator_title)
- [set_bot_commands](#set_bot_commands)
- [set_bot_default_privileges](#set_bot_default_privileges)
- [set_bot_info_description](#set_bot_info_description)
- [set_bot_info_short_description](#set_bot_info_short_description)
- [set_bot_name](#set_bot_name)
- [set_chat_accent_color](#set_chat_accent_color)
- [set_chat_description](#set_chat_description)
- [set_chat_direct_messages_group](#set_chat_direct_messages_group)
- [set_chat_discussion_group](#set_chat_discussion_group)
- [set_chat_member_tag](#set_chat_member_tag)
- [set_chat_menu_button](#set_chat_menu_button)
- [set_chat_permissions](#set_chat_permissions)
- [set_chat_photo](#set_chat_photo)
- [set_chat_profile_accent_color](#set_chat_profile_accent_color)
- [set_chat_protected_content](#set_chat_protected_content)
- [set_chat_title](#set_chat_title)
- [set_chat_ttl](#set_chat_ttl)
- [set_chat_username](#set_chat_username)
- [set_contact_note](#set_contact_note)
- [set_dc](#set_dc)
- [set_direct_messages_chat_topic_is_marked_as_unread](#set_direct_messages_chat_topic_is_marked_as_unread)
- [set_emoji_status](#set_emoji_status)
- [set_game_score](#set_game_score)
- [set_gift_collection_name](#set_gift_collection_name)
- [set_gift_resale_price](#set_gift_resale_price)
- [set_global_privacy_settings](#set_global_privacy_settings)
- [set_inactive_session_ttl](#set_inactive_session_ttl)
- [set_main_profile_tab](#set_main_profile_tab)
- [set_managed_bot_access_settings](#set_managed_bot_access_settings)
- [set_parse_mode](#set_parse_mode)
- [set_personal_channel](#set_personal_channel)
- [set_pinned_gifts](#set_pinned_gifts)
- [set_privacy](#set_privacy)
- [set_profile_audio_position](#set_profile_audio_position)
- [set_profile_photo](#set_profile_photo)
- [set_send_as_chat](#set_send_as_chat)
- [set_slow_mode](#set_slow_mode)
- [set_upgraded_gift_colors](#set_upgraded_gift_colors)
- [set_username](#set_username)
- [show_chat_stories](#show_chat_stories)
- [show_gift](#show_gift)
- [sign_in](#sign_in)
- [sign_in_bot](#sign_in_bot)
- [sign_up](#sign_up)
- [start](#start)
- [start_bot](#start_bot)
- [stop](#stop)
- [stop_poll](#stop_poll)
- [stop_transmission](#stop_transmission)
- [stream_media](#stream_media)
- [suggest_birthday](#suggest_birthday)
- [summarize_message](#summarize_message)
- [terminate](#terminate)
- [toggle_folder_tags](#toggle_folder_tags)
- [toggle_forum_topics](#toggle_forum_topics)
- [toggle_join_to_send](#toggle_join_to_send)
- [transfer_business_account_stars](#transfer_business_account_stars)
- [transfer_chat_ownership](#transfer_chat_ownership)
- [transfer_gift](#transfer_gift)
- [translate_message_text](#translate_message_text)
- [translate_text](#translate_text)
- [unarchive_chats](#unarchive_chats)
- [unban_chat_member](#unban_chat_member)
- [unblock_user](#unblock_user)
- [unpin_all_chat_messages](#unpin_all_chat_messages)
- [unpin_chat_message](#unpin_chat_message)
- [unpin_chat_stories](#unpin_chat_stories)
- [unpin_forum_topic](#unpin_forum_topic)
- [update_birthday](#update_birthday)
- [update_chat_notifications](#update_chat_notifications)
- [update_profile](#update_profile)
- [update_status](#update_status)
- [updates_watchdog](#updates_watchdog)
- [upgrade_gift](#upgrade_gift)
- [view_messages](#view_messages)
- [view_stories](#view_stories)
- [vote_poll](#vote_poll)

## Сигнатуры

### accept_terms_of_service

Доступен через client_call.

```python
accept_terms_of_service(self: 'pyrogram.Client', terms_of_service_id: 'str') -> 'bool'
```

Accept the given terms of service.

### add_chat_members

Доступен через client_call.

```python
add_chat_members(self: 'pyrogram.Client', chat_id: 'int | str', user_ids: 'int | str | list[int | str]', forward_limit: 'int' = 100) -> 'list[types.FailedToAddMember]'
```

Add new chat members to a group, supergroup or channel.
This method can't be used to join a chat. Members can't be added to a channel if it has more than 200 members.

### add_checklist_tasks

Доступен через client_call.

```python
add_checklist_tasks(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', tasks: 'list[types.InputChecklistTask]') -> 'int'
```

Add tasks to a checklist in a message.

### add_collection_gifts

Доступен через client_call.

```python
add_collection_gifts(self: 'pyrogram.Client', owner_id: 'int | str', collection_id: 'int', gift_ids: 'list[str]') -> 'types.GiftCollection'
```

Adds gifts to the beginning of a previously created collection.

### add_contact

Доступен через client_call.

```python
add_contact(self: 'pyrogram.Client', user_id: 'int | str', first_name: 'str', last_name: 'str' = '', phone_number: 'str' = '', share_phone_number: 'bool' = False, note: 'str | types.FormattedText | None' = None) -> 'types.User'
```

Add an existing Telegram user as contact, even without a phone number.

### add_handler

Синхронный метод: не доступен через асинхронный client_call.

```python
add_handler(self: 'pyrogram.Client', handler: 'Handler', group: 'int' = 0) -> 'tuple[Handler, int]'
```

Register an update handler.

### add_poll_option

Доступен через client_call.

```python
add_poll_option(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', option: 'str | types.InputPollOption') -> 'types.Message | bool'
```

Adds an option to a poll.

### add_profile_audio

Доступен через client_call.

```python
add_profile_audio(self: 'pyrogram.Client', audio: 'PathType | BinaryIO', duration: 'int' = 0, performer: 'str | None' = None, title: 'str | None' = None, thumb: 'PathType | BinaryIO | None' = None, file_name: 'str | None' = None, progress: 'Callable | None' = None, progress_args: 'tuple' = ()) -> 'bool | None'
```

Adds an audio file to the beginning of the profile audio files of the current user.

### add_to_gifs

Доступен через client_call.

```python
add_to_gifs(self: 'pyrogram.Client', file_id: 'str', unsave: 'bool' = False) -> 'bool'
```

Add a GIF to the list of saved GIFs.

### answer_callback_query

Доступен через client_call.

```python
answer_callback_query(self: 'pyrogram.Client', callback_query_id: 'str', text: 'str | None' = None, show_alert: 'bool | None' = None, url: 'str | None' = None, cache_time: 'int' = 0) -> 'bool'
```

Send answers to callback queries sent from inline keyboards.
The answer will be displayed to the user as a notification at the top of the chat screen or as an alert.

### answer_chat_join_request_query

Доступен через client_call.

```python
answer_chat_join_request_query(self: 'pyrogram.Client', chat_join_request_query_id: 'str', result: 'enums.ChatJoinRequestQueryResult') -> 'bool'
```

Use this method to process a received chat join request query.

### answer_guest_query

Доступен через client_call.

```python
answer_guest_query(self: 'pyrogram.Client', guest_query_id: 'str', result: 'types.InlineQueryResult') -> 'types.SentGuestMessage'
```

Use this method to reply to a received guest message.

### answer_inline_query

Доступен через client_call.

```python
answer_inline_query(self: 'pyrogram.Client', inline_query_id: 'str', results: 'Iterable[types.InlineQueryResult]', cache_time: 'int' = 300, is_gallery: 'bool' = False, is_personal: 'bool' = False, next_offset: 'str' = '', switch_pm_text: 'str' = '', switch_pm_parameter: 'str' = '') -> 'bool'
```

Send answers to an inline query.

### answer_pre_checkout_query

Доступен через client_call.

```python
answer_pre_checkout_query(self: 'pyrogram.Client', pre_checkout_query_id: 'str', ok: 'bool | None' = None, error_message: 'str | None' = None) -> 'bool'
```

Send answers to pre-checkout queries.

### answer_shipping_query

Доступен через client_call.

```python
answer_shipping_query(self: 'pyrogram.Client', shipping_query_id: 'str', ok: 'bool', shipping_options: 'list[types.ShippingOption] | None' = None, error_message: 'str | None' = None) -> 'bool'
```

If you sent an invoice requesting a shipping address and the parameter ``is_flexible`` was specified, the API sends the confirmation in the form of an :obj:`~pyrogram.handlers.ShippingQueryHandler`.

### answer_web_app_query

Доступен через client_call.

```python
answer_web_app_query(self: 'pyrogram.Client', web_app_query_id: 'str', result: 'types.InlineQueryResult') -> 'types.SentWebAppMessage'
```

Set the result of an interaction with a `Web App <https://core.telegram.org/bots/webapps>`_ and send a
corresponding message on behalf of the user to the chat from which the query originated.

### apply_boost

Доступен через client_call.

```python
apply_boost(self: 'pyrogram.Client', chat_id: 'int | str') -> 'bool'
```

Apply boost

### apply_gift_code

Доступен через client_call.

```python
apply_gift_code(self: 'pyrogram.Client', link: 'str') -> 'bool'
```

Apply a gift code.

### approve_all_chat_join_requests

Доступен через client_call.

```python
approve_all_chat_join_requests(self: 'pyrogram.Client', chat_id: 'int | str', invite_link: 'str | None' = None) -> 'bool'
```

Approve all pending join requests in a chat.

### approve_chat_join_request

Доступен через client_call.

```python
approve_chat_join_request(self: 'pyrogram.Client', chat_id: 'int | str', user_id: 'int') -> 'bool'
```

Approve a chat join request.

### approve_suggested_post

Доступен через client_call.

```python
approve_suggested_post(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', send_date: 'datetime | None' = None) -> 'bool'
```

Use this method to approve a suggested post in a direct messages chat.

### archive_chats

Доступен через client_call.

```python
archive_chats(self: 'pyrogram.Client', chat_ids: 'int | str | list[int | str]') -> 'bool'
```

Archive one or more chats.

### authorize

Недоступен через client_call: исключён политикой моста.

```python
authorize(self) -> 'User'
```



### authorize_qr

Доступен через client_call.

```python
authorize_qr(self, except_ids: 'list[int] | None' = None) -> 'User'
```



### ban_chat_member

Доступен через client_call.

```python
ban_chat_member(self: 'pyrogram.Client', chat_id: 'int | str', user_id: 'int | str', until_date: 'datetime | None' = None, revoke_messages: 'bool | None' = None, revoke_reactions: 'bool | None' = None) -> 'types.Message | bool'
```

Ban a user from a group, a supergroup or a channel.
In the case of supergroups and channels, the user will not be able to return to the group on their own using
invite links, etc., unless unbanned first. You must be an a

### block_user

Доступен через client_call.

```python
block_user(self: 'pyrogram.Client', user_id: 'int | str') -> 'bool'
```

Block a user.

### buy_gift_upgrade

Доступен через client_call.

```python
buy_gift_upgrade(self: 'pyrogram.Client', owner_id: 'int | str', prepaid_upgrade_hash: 'str', star_count: 'int') -> 'bool'
```

Pays for upgrade of a regular gift that is owned by another user or channel chat.

### can_post_stories

Доступен через client_call.

```python
can_post_stories(self: 'pyrogram.Client', chat_id: 'int | str') -> 'int'
```

Check whether we can post stories as the specified chat.

### change_cloud_password

Доступен через client_call.

```python
change_cloud_password(self: 'pyrogram.Client', current_password: 'str', new_password: 'str', new_hint: 'str' = '') -> 'bool'
```

Change your Two-Step Verification password (Cloud Password) with a new one.

### change_phone_number

Доступен через client_call.

```python
change_phone_number(self: 'pyrogram.Client', phone_number: 'str', phone_code_hash: 'str', phone_code: 'str') -> 'types.User'
```

Change a user phone number in Telegram with a valid confirmation code.

### check_bot_username

Доступен через client_call.

```python
check_bot_username(self: 'pyrogram.Client', username: 'str') -> 'types.User'
```

Checks whether a username can be set for a new bot.

### check_chat_folder_invite_link

Доступен через client_call.

```python
check_chat_folder_invite_link(self: 'pyrogram.Client', invite_link: 'str') -> 'types.ChatFolderInviteLinkInfo'
```

Checks the validity of an invite link for a chat folder and returns information about the corresponding chat folder.

### check_gift_code

Доступен через client_call.

```python
check_gift_code(self: 'pyrogram.Client', link: 'str') -> 'types.CheckedGiftCode'
```

Get information about a gift code.

### check_password

Недоступен через client_call: исключён политикой моста.

```python
check_password(self: 'pyrogram.Client', password: 'str') -> 'types.User'
```

Check your Two-Step Verification password and log in.

### check_username

Доступен через client_call.

```python
check_username(self: 'pyrogram.Client', chat_id: 'int | str', username: 'str') -> 'bool'
```

Check if a username is available.

### close_forum_topic

Доступен через client_call.

```python
close_forum_topic(self: 'pyrogram.Client', chat_id: 'int | str', topic_id: 'int') -> 'bool'
```

Close a forum topic.

### compose_text_with_ai

Доступен через client_call.

```python
compose_text_with_ai(self: 'pyrogram.Client', text: 'str | types.FormattedText', translate_to_language_code: 'str | None' = None, style_name: 'str | None' = None, add_emojis: 'bool | None' = None) -> 'types.FormattedText'
```

Changes text using an AI model.

### connect

Недоступен через client_call: исключён политикой моста.

```python
connect(self: 'pyrogram.Client') -> 'bool'
```

Connect the client to Telegram servers.

### convert_gift_to_stars

Доступен через client_call.

```python
convert_gift_to_stars(self: 'pyrogram.Client', owned_gift_id: 'str', business_connection_id: 'str | None' = None) -> 'bool'
```

Convert a given regular gift to Telegram Stars.

### copy_media_group

Доступен через client_call.

```python
copy_media_group(self: 'pyrogram.Client', chat_id: 'int | str', from_chat_id: 'int | str', message_id: 'int', captions: 'list[str] | str | None' = None, has_spoilers: 'list[bool] | bool | None' = None, disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, schedule_date: 'datetime | None' = None, protect_content: 'bool | None' = None, show_caption_above_media: 'bool | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, reply_to_story_id: 'int | None' = None, quote_text: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'list[types.Message]'
```

Copy a media group by providing one of the message ids.

### copy_message

Доступен через client_call.

```python
copy_message(self: 'pyrogram.Client', chat_id: 'int | str', from_chat_id: 'int | str', message_id: 'int', caption: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None, disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, schedule_date: 'datetime | None' = None, protect_content: 'bool | None' = None, has_spoiler: 'bool | None' = None, show_caption_above_media: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None | type[object]' = <class 'object'>, reply_to_chat_id: 'int | str | None' = None, reply_to_message_id: 'int | None' = None, quote_text: 'str | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None) -> 'types.Message | None'
```

Copy messages of any kind.

### copy_story

Доступен через client_call.

```python
copy_story(self: 'pyrogram.Client', chat_id: 'int | str', from_chat_id: 'int | str', story_id: 'int', caption: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None, period: 'int | None' = None, privacy: 'enums.StoriesPrivacyRules | None' = None, allowed_users: 'list[int | str] | None' = None, disallowed_users: 'list[int | str] | None' = None, protect_content: 'bool | None' = None) -> 'types.Story | None'
```

Copy story.

### craft_gift

Доступен через client_call.

```python
craft_gift(self: 'pyrogram.Client', owned_gift_ids: 'list[str]') -> 'types.CraftGiftResult'
```

Crafts a new gift from other gifts that will be permanently lost.

### create_bot

Доступен через client_call.

```python
create_bot(self: 'pyrogram.Client', manager_bot_user_id: 'int | str', name: 'str', username: 'str', via_link: 'bool | None' = None) -> 'types.User'
```

Creates a bot which will be managed by another bot.

### create_channel

Доступен через client_call.

```python
create_channel(self: 'pyrogram.Client', title: 'str', description: 'str' = '') -> 'types.Chat'
```

Create a new broadcast channel.

### create_chat_invite_link

Доступен через client_call.

```python
create_chat_invite_link(self: 'pyrogram.Client', chat_id: 'int | str', name: 'str | None' = None, expire_date: 'datetime | None' = None, member_limit: 'int | None' = None, creates_join_request: 'bool | None' = None) -> 'types.ChatInviteLink | None'
```

Create an additional invite link for a chat.

### create_folder

Доступен через client_call.

```python
create_folder(self: 'pyrogram.Client', name: 'str', parse_mode: 'enums.ParseMode | None' = None, entities: 'list[types.MessageEntity] | None' = None, animate_custom_emoji: 'bool | None' = None, icon: 'str | None' = None, color: 'enums.FolderColor | None' = None, pinned_chats: 'list[int | str] | None' = None, included_chats: 'list[int | str] | None' = None, excluded_chats: 'list[int | str] | None' = None, exclude_muted: 'bool | None' = None, exclude_read: 'bool | None' = None, exclude_archived: 'bool | None' = None, include_contacts: 'bool | None' = None, include_non_contacts: 'bool | None' = None, include_bots: 'bool | None' = None, include_groups: 'bool | None' = None, include_channels: 'bool | None' = None) -> 'int'
```

Create new chat folder.

### create_folder_invite_link

Доступен через client_call.

```python
create_folder_invite_link(self: 'pyrogram.Client', chat_folder_id: 'int', chat_ids: 'list[int | str]', name: 'str | None' = None) -> 'types.FolderInviteLink'
```

Create a new invite link for a chat folder.

### create_forum_topic

Доступен через client_call.

```python
create_forum_topic(self: 'pyrogram.Client', chat_id: 'int | str', title: 'str', icon_color: 'int | None' = None, icon_emoji_id: 'int | None' = None) -> 'types.ForumTopicCreated'
```

Create a new forum topic.

### create_gift_collection

Доступен через client_call.

```python
create_gift_collection(self: 'pyrogram.Client', owner_id: 'int | str', name: 'str', gift_ids: 'list[str]') -> 'types.GiftCollection'
```

Creates a collection from gifts on the current user's or a channel's profile page.

### create_group

Доступен через client_call.

```python
create_group(self: 'pyrogram.Client', title: 'str', users: 'int | str | list[int | str]') -> 'types.Chat'
```

Create a new basic group.

### create_invoice_link

Доступен через client_call.

```python
create_invoice_link(self: 'pyrogram.Client', title: 'str', description: 'str', payload: 'str | bytes', currency: 'str', prices: 'list[types.LabeledPrice]', provider_token: 'str | None' = None, subscription_period: 'int | None' = None, max_tip_amount: 'int | None' = None, suggested_tip_amounts: 'list[int] | None' = None, start_parameter: 'str | None' = None, provider_data: 'str | None' = None, photo_url: 'str | None' = None, photo_size: 'int | None' = None, photo_width: 'int | None' = None, photo_height: 'int | None' = None, need_name: 'bool | None' = None, need_phone_number: 'bool | None' = None, need_email: 'bool | None' = None, need_shipping_address: 'bool | None' = None, send_phone_number_to_provider: 'bool | None' = None, send_email_to_provider: 'bool | None' = None, is_flexible: 'bool | None' = None) -> 'str'
```

Create invoice link.

### create_supergroup

Доступен через client_call.

```python
create_supergroup(self: 'pyrogram.Client', title: 'str', description: 'str' = '', is_forum: 'bool | None' = None, message_auto_delete_time: 'int | None' = None, for_import: 'bool | None' = None) -> 'types.Chat'
```

Create a new supergroup.

### decline_all_chat_join_requests

Доступен через client_call.

```python
decline_all_chat_join_requests(self: 'pyrogram.Client', chat_id: 'int | str', invite_link: 'str | None' = None) -> 'bool'
```

Decline all pending join requests in a chat.

### decline_chat_join_request

Доступен через client_call.

```python
decline_chat_join_request(self: 'pyrogram.Client', chat_id: 'int | str', user_id: 'int') -> 'bool'
```

Decline a chat join request.

### decline_suggested_post

Доступен через client_call.

```python
decline_suggested_post(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', comment: 'str | None' = None) -> 'bool'
```

Use this method to decline a suggested post in a direct messages chat.

### delete_all_message_reactions

Доступен через client_call.

```python
delete_all_message_reactions(self: 'pyrogram.Client', chat_id: 'int | str', *, user_id: 'int | str | None' = None, actor_chat_id: 'int | str | None' = None) -> 'bool'
```

Use this method to remove up to 10000 recent reactions in a group or a supergroup chat added by a given user or chat.

### delete_bot_commands

Доступен через client_call.

```python
delete_bot_commands(self: 'pyrogram.Client', scope: 'types.BotCommandScope | None' = None, language_code: 'str' = '') -> 'bool'
```

Delete the list of the bot's commands for the given scope and user language.
After deletion, higher level commands will be shown to affected users.

### delete_business_messages

Доступен через client_call.

```python
delete_business_messages(self: 'pyrogram.Client', business_connection_id: 'str', message_ids: 'int | Iterable[int]') -> 'int'
```

Delete messages on behalf of a business account.

### delete_channel

Доступен через client_call.

```python
delete_channel(self: 'pyrogram.Client', chat_id: 'int | str') -> 'bool'
```

Delete a channel.

### delete_chat_admin_invite_links

Доступен через client_call.

```python
delete_chat_admin_invite_links(self: 'pyrogram.Client', chat_id: 'int | str', admin_id: 'int | str') -> 'bool'
```

Delete all revoked invite links of an administrator.

### delete_chat_history

Доступен через client_call.

```python
delete_chat_history(self: 'pyrogram.Client', chat_id: 'int | str', max_id: 'int' = 0, revoke: 'bool | None' = None, just_clear=None, min_date: 'datetime | None' = None, max_date: 'datetime | None' = None) -> 'int'
```

Delete the history of a chat.

### delete_chat_invite_link

Доступен через client_call.

```python
delete_chat_invite_link(self: 'pyrogram.Client', chat_id: 'int | str', invite_link: 'str') -> 'bool'
```

Delete an already revoked invite link.

### delete_chat_photo

Доступен через client_call.

```python
delete_chat_photo(self: 'pyrogram.Client', chat_id: 'int | str') -> 'bool'
```

Delete a chat photo.

### delete_contacts

Доступен через client_call.

```python
delete_contacts(self: 'pyrogram.Client', user_ids: 'int | str | list[int | str]') -> 'types.User | list[types.User] | None'
```

Delete contacts from your Telegram address book.

### delete_direct_messages_chat_topic_history

Доступен через client_call.

```python
delete_direct_messages_chat_topic_history(self: 'pyrogram.Client', chat_id: 'int | str', topic_id: 'int | None' = None, max_id: 'int' = 0, min_date: 'datetime | None' = None, max_date: 'datetime | None' = None) -> 'int'
```

Delete messages in the topic in a channel direct messages chat administered by the current user.

### delete_ephemeral_message

Доступен через client_call.

```python
delete_ephemeral_message(self: 'pyrogram.Client', chat_id: 'int | str', receiver_user_id: 'int | str', ephemeral_message_id: 'int') -> 'bool'
```

Use this method to delete an ephemeral message.
Note that it is not guaranteed that the user will receive the message deletion event, especially if they are offline.

### delete_folder

Доступен через client_call.

```python
delete_folder(self: 'pyrogram.Client', folder_id: 'int') -> 'bool'
```

Delete a user's folder.

### delete_folder_invite_link

Доступен через client_call.

```python
delete_folder_invite_link(self: 'pyrogram.Client', chat_folder_id: 'int', invite_link: 'str') -> 'bool'
```

Deletes an invite link for a chat folder.

### delete_forum_topic

Доступен через client_call.

```python
delete_forum_topic(self: 'pyrogram.Client', chat_id: 'int | str', topic_id: 'int') -> 'bool'
```

Delete a forum topic.

### delete_gift_collection

Доступен через client_call.

```python
delete_gift_collection(self: 'pyrogram.Client', owner_id: 'int | str', collection_id: 'int') -> 'types.GiftCollection'
```

Deletes a gift collection.

### delete_message_reaction

Доступен через client_call.

```python
delete_message_reaction(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', *, user_id: 'int | str | None' = None, actor_chat_id: 'int | str | None' = None) -> 'bool'
```

Use this method to remove a reaction from a message in a group or a supergroup chat.

### delete_messages

Доступен через client_call.

```python
delete_messages(self: 'pyrogram.Client', chat_id: 'int | str', message_ids: 'int | Iterable[int]', revoke: 'bool' = True, is_scheduled: 'bool | None' = None) -> 'int'
```

Delete messages, including service messages.

### delete_poll_option

Доступен через client_call.

```python
delete_poll_option(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', option: 'str | types.InputPollOption') -> 'types.Message | bool'
```

Deletes an option from a poll.

### delete_profile_photos

Доступен через client_call.

```python
delete_profile_photos(self: 'pyrogram.Client', photo_ids: 'str | list[str]') -> 'bool'
```

Delete your own profile photos.

### delete_stories

Доступен через client_call.

```python
delete_stories(self: 'pyrogram.Client', chat_id: 'int | str', story_ids: 'int | Iterable[int]') -> 'list[int]'
```

Delete posted stories.

### delete_supergroup

Доступен через client_call.

```python
delete_supergroup(self: 'pyrogram.Client', chat_id: 'int | str') -> 'bool'
```

Delete a supergroup.

### delete_user_history

Доступен через client_call.

```python
delete_user_history(self: 'pyrogram.Client', chat_id: 'int | str', user_id: 'int | str') -> 'bool'
```

Delete all messages sent by a certain user in a supergroup.

### disconnect

Недоступен через client_call: исключён политикой моста.

```python
disconnect(self: 'pyrogram.Client')
```

Disconnect the client from Telegram servers.

### download_media

Доступен через client_call.

```python
download_media(self: 'pyrogram.Client', message: 'str | types.Message | types.Story | types.Audio | types.Document | types.Photo | types.Sticker | types.Animation | types.Video | types.Voice | types.VideoNote | types.PaidMediaInfo | types.Thumbnail | types.StrippedThumbnail | types.PaidMediaPreview | types.ChatPhoto', file_name: 'PathType' = 'downloads/', in_memory: 'bool' = False, block: 'bool' = True, progress: 'Callable | None' = None, progress_args: 'tuple' = ()) -> 'str | BinaryIO | list[str] | list[BinaryIO] | None'
```

Download the media from a message.

### drop_gift_original_details

Доступен через client_call.

```python
drop_gift_original_details(self: 'pyrogram.Client', owned_gift_id: 'str', star_count: 'int | None' = None) -> 'bool'
```

Drops original details for an upgraded gift.

### edit_chat_invite_link

Доступен через client_call.

```python
edit_chat_invite_link(self: 'pyrogram.Client', chat_id: 'int | str', invite_link: 'str', name: 'str | None' = None, expire_date: 'datetime | None' = None, member_limit: 'int | None' = None, creates_join_request: 'bool | None' = None) -> 'types.ChatInviteLink | None'
```

Edit a non-primary invite link.

### edit_ephemeral_message_caption

Доступен через client_call.

```python
edit_ephemeral_message_caption(self: 'pyrogram.Client', chat_id: 'int | str', receiver_user_id: 'int | str', ephemeral_message_id: 'int', caption: 'str' = '', parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None, show_caption_above_media: 'bool | None' = None, reply_markup: 'types.InlineKeyboardMarkup | None' = None) -> 'types.Message | None'
```

Use this method to edit the caption of an ephemeral message.
Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline.

### edit_ephemeral_message_media

Доступен через client_call.

```python
edit_ephemeral_message_media(self: 'pyrogram.Client', chat_id: 'int | str', receiver_user_id: 'int | str', ephemeral_message_id: 'int', media: 'types.InputMedia', reply_markup: 'types.InlineKeyboardMarkup | None' = None) -> 'types.Message | None'
```

Use this method to edit the media of an ephemeral message.
Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline.

### edit_ephemeral_message_reply_markup

Доступен через client_call.

```python
edit_ephemeral_message_reply_markup(self: 'pyrogram.Client', chat_id: 'int | str', receiver_user_id: 'int | str', ephemeral_message_id: 'int', reply_markup: 'types.InlineKeyboardMarkup | None' = None) -> 'types.Message | None'
```

Use this method to edit only the reply markup of an ephemeral message.
Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline.

### edit_ephemeral_message_text

Доступен через client_call.

```python
edit_ephemeral_message_text(self: 'pyrogram.Client', chat_id: 'int | str', receiver_user_id: 'int | str', ephemeral_message_id: 'int', text: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, entities: 'list[types.MessageEntity] | None' = None, rich_message: 'types.InputRichMessage | None' = None, link_preview_options: 'types.LinkPreviewOptions | None' = None, reply_markup: 'types.InlineKeyboardMarkup | None' = None) -> 'types.Message | None'
```

Use this method to edit an ephemeral text message.
Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline.

### edit_folder

Доступен через client_call.

```python
edit_folder(self: 'pyrogram.Client', folder_id: 'int', name: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, entities: 'list[types.MessageEntity] | None' = None, animate_custom_emoji: 'bool | None' = None, icon: 'str | None' = None, color: 'enums.FolderColor | None' = None, pinned_chats: 'list[int | str] | None' = None, included_chats: 'list[int | str] | None' = None, excluded_chats: 'list[int | str] | None' = None, exclude_muted: 'bool | None' = None, exclude_read: 'bool | None' = None, exclude_archived: 'bool | None' = None, include_contacts: 'bool | None' = None, include_non_contacts: 'bool | None' = None, include_bots: 'bool | None' = None, include_groups: 'bool | None' = None, include_channels: 'bool | None' = None) -> 'bool'
```

Update chat folder.

### edit_forum_topic

Доступен через client_call.

```python
edit_forum_topic(self: 'pyrogram.Client', chat_id: 'int | str', topic_id: 'int', title: 'str | None' = None, icon_emoji_id: 'int | None' = None, closed: 'bool | None' = None, hidden: 'bool | None' = None) -> 'bool'
```

Edit a forum topic.

### edit_inline_caption

Доступен через client_call.

```python
edit_inline_caption(self: 'pyrogram.Client', inline_message_id: 'str', caption: 'str', parse_mode: 'enums.ParseMode | None' = None, reply_markup: 'types.InlineKeyboardMarkup | None' = None) -> 'bool'
```

Edit the caption of inline media messages.

### edit_inline_media

Доступен через client_call.

```python
edit_inline_media(self: 'pyrogram.Client', inline_message_id: 'str', media: 'types.InputMedia', reply_markup: 'types.InlineKeyboardMarkup | None' = None) -> 'bool'
```

Edit inline animation, audio, document, photo or video messages, or to add media to text messages.

### edit_inline_reply_markup

Доступен через client_call.

```python
edit_inline_reply_markup(self: 'pyrogram.Client', inline_message_id: 'str', reply_markup: 'types.InlineKeyboardMarkup | None' = None) -> 'bool'
```

Edit only the reply markup of inline messages sent via the bot (for inline bots).

### edit_inline_text

Доступен через client_call.

```python
edit_inline_text(self: 'pyrogram.Client', inline_message_id: 'str', text: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, link_preview_options: 'types.LinkPreviewOptions | None' = None, entities: 'list[types.MessageEntity] | None' = None, rich_message: 'types.InputRichMessage | None' = None, reply_markup: 'types.InlineKeyboardMarkup | None' = None, disable_web_page_preview: 'bool | None' = None) -> 'bool'
```

Edit the text of inline messages.

### edit_message_caption

Доступен через client_call.

```python
edit_message_caption(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', caption: 'str', parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None, schedule_date: 'datetime | None' = None, business_connection_id: 'str | None' = None, show_caption_above_media: 'bool | None' = None, reply_markup: 'types.InlineKeyboardMarkup | None' = None) -> 'types.Message'
```

Edit the caption of media messages.

### edit_message_checklist

Доступен через client_call.

```python
edit_message_checklist(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', checklist: 'types.InputChecklist', business_connection_id: 'str | None' = None, reply_markup: 'types.InlineKeyboardMarkup | None' = None) -> 'types.Message'
```

Use this method to edit a checklist.

### edit_message_media

Доступен через client_call.

```python
edit_message_media(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', media: 'types.InputMedia', show_caption_above_media: 'bool | None' = None, schedule_date: 'datetime | None' = None, business_connection_id: 'str | None' = None, reply_markup: 'types.InlineKeyboardMarkup | None' = None) -> 'types.Message'
```

Edit animation, audio, document, photo or video messages, or to add media to text messages.

### edit_message_reply_markup

Доступен через client_call.

```python
edit_message_reply_markup(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', schedule_date: 'datetime | None' = None, reply_markup: 'types.InlineKeyboardMarkup | None' = None) -> 'types.Message'
```

Edit only the reply markup of messages sent by the bot.

### edit_message_text

Доступен через client_call.

```python
edit_message_text(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', text: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, entities: 'list[types.MessageEntity] | None' = None, link_preview_options: 'types.LinkPreviewOptions | None' = None, schedule_date: 'datetime | None' = None, business_connection_id: 'str | None' = None, rich_message: 'types.InputRichMessage | None' = None, reply_markup: 'types.InlineKeyboardMarkup | None' = None, show_caption_above_media: 'bool | None' = None, disable_web_page_preview: 'bool | None' = None) -> 'types.Message'
```

Edit the text of messages.

### edit_star_subscription

Доступен через client_call.

```python
edit_star_subscription(self: 'pyrogram.Client', subscription_id: 'str', is_canceled: 'bool') -> 'bool'
```

Cancels or re-enables Telegram Star subscription.

### edit_story_caption

Доступен через client_call.

```python
edit_story_caption(self: 'pyrogram.Client', chat_id: 'int | str', story_id: 'int', caption: 'str', parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None) -> 'types.Story'
```

Edit the caption of story.

### edit_story_media

Доступен через client_call.

```python
edit_story_media(self: 'pyrogram.Client', chat_id: 'int | str', story_id: 'int', media: 'PathType | BinaryIO | None' = None, media_areas: 'list[types.MediaArea] | None' = None, duration: 'int' = 0, width: 'int' = 0, height: 'int' = 0, thumb: 'PathType | BinaryIO | None' = None, supports_streaming: 'bool' = True, file_name: 'str | None' = None, progress: 'Callable | None' = None, progress_args: 'tuple' = ()) -> 'types.Story | None'
```

Edit story media.

### edit_story_privacy

Доступен через client_call.

```python
edit_story_privacy(self: 'pyrogram.Client', chat_id: 'int | str', story_id: 'int', privacy: 'enums.StoriesPrivacyRules' = pyrogram.enums.StoriesPrivacyRules.PUBLIC, allowed_users: 'list[int | str] | None' = None, disallowed_users: 'list[int | str] | None' = None) -> 'types.Story'
```

Edit the privacy of story.

### edit_user_star_subscription

Доступен через client_call.

```python
edit_user_star_subscription(self: 'pyrogram.Client', user_id: 'int | str', telegram_payment_charge_id: 'str', is_canceled: 'bool') -> 'bool'
```

Cancels or re-enables Telegram Star subscription for a user.

### enable_cloud_password

Доступен через client_call.

```python
enable_cloud_password(self: 'pyrogram.Client', password: 'str', hint: 'str' = '', email: 'str | None' = None) -> 'bool'
```

Enable the Two-Step Verification security feature (Cloud Password) on your account.

### enable_stealth_mode

Доступен через client_call.

```python
enable_stealth_mode(self: 'pyrogram.Client', past: 'bool | None' = None, future: 'bool | None' = None) -> 'types.StoriesStealthMode'
```

Activates stories stealth mode.

### export_chat_invite_link

Доступен через client_call.

```python
export_chat_invite_link(self: 'pyrogram.Client', chat_id: 'int | str') -> 'types.ChatInviteLink'
```

Generate a new primary invite link for a chat; any previously generated primary link is revoked.

### export_session_string

Недоступен через client_call: исключён политикой моста.

```python
export_session_string(self: 'pyrogram.Client') -> 'str'
```

Export the current authorized session as a serialized string.

### fetch_peers

Доступен через client_call.

```python
fetch_peers(self, peers: 'list[raw.base.User | raw.base.Chat]') -> 'bool'
```



### fix_text_with_ai

Доступен через client_call.

```python
fix_text_with_ai(self: 'pyrogram.Client', text: 'str | types.FormattedText') -> 'types.FormattedText'
```

Fixes text using an AI model.

### forward_media_group

Доступен через client_call.

```python
forward_media_group(self: 'pyrogram.Client', chat_id: 'int | str', from_chat_id: 'int | str', message_id: 'int', message_thread_id: 'int | None' = None, disable_notification: 'bool | None' = None, schedule_date: 'datetime | None' = None, hide_sender_name: 'bool | None' = None, hide_captions: 'bool | None' = None, protect_content: 'bool | None' = None, allow_paid_broadcast: 'bool | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, paid_message_star_count: 'int | None' = None) -> 'list[types.Message]'
```

Forward a media group by providing one of the message ids.

### forward_messages

Доступен через client_call.

```python
forward_messages(self: 'pyrogram.Client', chat_id: 'int | str', from_chat_id: 'int | str', message_ids: 'int | Iterable[int]', message_thread_id: 'int | None' = None, disable_notification: 'bool | None' = None, schedule_date: 'datetime | None' = None, repeat_period: 'int | None' = None, hide_sender_name: 'bool | None' = None, hide_captions: 'bool | None' = None, protect_content: 'bool | None' = None, allow_paid_broadcast: 'bool | None' = None, video_start_timestamp: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, paid_message_star_count: 'int | None' = None) -> 'types.Message | list[types.Message] | None'
```

Forward messages of any kind.

### forward_story

Доступен через client_call.

```python
forward_story(self: 'pyrogram.Client', chat_id: 'int | str', from_chat_id: 'int | str', story_id: 'int', disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, schedule_date: 'datetime | None' = None, repeat_period: 'int | None' = None, paid_message_star_count: 'int | None' = None, protect_content: 'bool | None' = None, allow_paid_broadcast: 'bool | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, message_effect_id: 'int | None' = None) -> 'types.Message | None'
```

Forward story.

### get_account_ttl

Доступен через client_call.

```python
get_account_ttl(self: 'pyrogram.Client') -> 'int'
```

Get days to live of account.

### get_active_sessions

Доступен через client_call.

```python
get_active_sessions(self: 'pyrogram.Client') -> 'types.ActiveSessions'
```

Returns all active sessions of the current user.

### get_all_stories

Доступен через client_call.

```python
get_all_stories(self: 'pyrogram.Client', next: 'bool | None' = None, hidden: 'bool | None' = None, state: 'str | None' = None) -> 'AsyncGenerator[types.Story, None]'
```

Get all active or hidden stories that displayed on the action bar on the homescreen.

### get_archived_stories

Доступен через client_call.

```python
get_archived_stories(self: 'pyrogram.Client', chat_id: 'int | str', limit: 'int' = 0, offset_id: 'int' = 0) -> 'AsyncGenerator[types.Story, None]'
```

Get all archived stories from a chat by using chat identifier.

### get_available_effects

Доступен через client_call.

```python
get_available_effects(self: 'pyrogram.Client') -> 'list[types.AvailableEffect]'
```

Get all available effects.

### get_available_gifts

Доступен через client_call.

```python
get_available_gifts(self: 'pyrogram.Client') -> 'list[types.Gift]'
```

Get all available star gifts that can be sent to other users.

### get_blocked_message_senders

Доступен через client_call.

```python
get_blocked_message_senders(self: 'pyrogram.Client', block_list: 'enums.BlockList' = pyrogram.enums.BlockList.MAIN, offset: 'int' = 0, limit: 'int' = 0) -> 'AsyncGenerator[types.Chat, None]'
```

Returns users and chats that were blocked by the current user.

### get_boosts

Доступен через client_call.

```python
get_boosts(self: 'pyrogram.Client') -> 'list[types.MyBoost]'
```

Get your boosts list

### get_boosts_status

Доступен через client_call.

```python
get_boosts_status(self: 'pyrogram.Client', chat_id: 'int | str') -> 'types.BoostsStatus'
```

Get boosts status of channel

### get_bot_commands

Доступен через client_call.

```python
get_bot_commands(self: 'pyrogram.Client', scope: 'types.BotCommandScope | None' = None, language_code: 'str' = '') -> 'list[types.BotCommand]'
```

Get the current list of the bot's commands for the given scope and user language.
Returns Array of BotCommand on success. If commands aren't set, an empty list is returned.

### get_bot_default_privileges

Доступен через client_call.

```python
get_bot_default_privileges(self: 'pyrogram.Client', for_channels: 'bool | None' = None) -> 'types.ChatAdministratorRights | None'
```

Get the current default privileges of the bot.

### get_bot_info_description

Доступен через client_call.

```python
get_bot_info_description(self: 'pyrogram.Client', language_code: 'str' = '', for_my_bot: 'int | str | None' = None) -> 'str'
```

Use this method to get the current / owned bot description for the given user language.

### get_bot_info_short_description

Доступен через client_call.

```python
get_bot_info_short_description(self: 'pyrogram.Client', language_code: 'str' = '', for_my_bot: 'int | str | None' = None) -> 'str'
```

Use this method to get the current / owned bot short description for the given user language.

### get_bot_name

Доступен через client_call.

```python
get_bot_name(self: 'pyrogram.Client', language_code: 'str' = '', for_my_bot: 'int | str | None' = None) -> 'str'
```

Use this method to get the current / owned bot name for the given user language.

### get_business_account_gifts

Доступен через client_call.

```python
get_business_account_gifts(self: 'pyrogram.Client', business_connection_id: 'str', collection_id: 'int | None' = None, exclude_unsaved: 'bool | None' = None, exclude_saved: 'bool | None' = None, exclude_unlimited: 'bool | None' = None, exclude_upgradable: 'bool | None' = None, exclude_non_upgradable: 'bool | None' = None, exclude_upgraded: 'bool | None' = None, exclude_without_colors: 'bool | None' = None, exclude_hosted: 'bool | None' = None, sort_by_price: 'bool | None' = None, limit: 'int' = 0, offset: 'str' = '') -> 'AsyncGenerator[types.Gift, None]'
```

Return the gifts received and owned by a managed business account.

### get_business_account_star_balance

Доступен через client_call.

```python
get_business_account_star_balance(self: 'pyrogram.Client', business_connection_id: 'str') -> 'int'
```

Return the amount of Telegram Stars owned by a managed business account.

### get_business_connection

Доступен через client_call.

```python
get_business_connection(self: 'pyrogram.Client', business_connection_id: 'str') -> 'types.BusinessConnection'
```

Use this method to get information about the connection of the bot with a business account.

### get_call_members

Доступен через client_call.

```python
get_call_members(self: 'pyrogram.Client', chat_id: 'int | str', limit: 'int' = 0) -> 'AsyncGenerator[types.GroupCallMember, None]'
```

Get the members list of a chat call.

### get_chat

Доступен через client_call.

```python
get_chat(self: 'pyrogram.Client', chat_id: 'int | str', force_full: 'bool' = True) -> 'types.Chat | None'
```

Get up to date information about a chat.

### get_chat_admin_invite_links

Доступен через client_call.

```python
get_chat_admin_invite_links(self: 'pyrogram.Client', chat_id: 'int | str', admin_id: 'int | str', revoked: 'bool' = False, limit: 'int' = 0) -> 'AsyncGenerator[types.ChatInviteLink, None]'
```

Get the invite links created by an administrator in a chat.

### get_chat_admin_invite_links_count

Доступен через client_call.

```python
get_chat_admin_invite_links_count(self: 'pyrogram.Client', chat_id: 'int | str', admin_id: 'int | str', revoked: 'bool' = False) -> 'int'
```

Get the count of the invite links created by an administrator in a chat.

### get_chat_admins_with_invite_links

Доступен через client_call.

```python
get_chat_admins_with_invite_links(self: 'pyrogram.Client', chat_id: 'int | str') -> 'list[types.ChatAdminWithInviteLinks]'
```

Get the list of the administrators that have exported invite links in a chat.

### get_chat_audios

Доступен через client_call.

```python
get_chat_audios(self: 'pyrogram.Client', chat_id: 'int | str', limit: 'int' = 0) -> 'AsyncGenerator[types.Audio, None]'
```

Get a user profile audios sequentially.

### get_chat_audios_count

Доступен через client_call.

```python
get_chat_audios_count(self: 'pyrogram.Client', chat_id: 'int | str') -> 'int'
```

Get the total count of audios for a chat.

### get_chat_event_log

Доступен через client_call.

```python
get_chat_event_log(self: 'pyrogram.Client', chat_id: 'int | str', query: 'str' = '', offset_id: 'int' = 0, limit: 'int' = 0, filters: 'types.ChatEventFilter | None' = None, user_ids: 'list[int | str] | None' = None) -> 'AsyncGenerator[types.ChatEvent, None]'
```

Get the actions taken by chat members and administrators in the last 48h.

### get_chat_gifts

Доступен через client_call.

```python
get_chat_gifts(self: 'pyrogram.Client', chat_id: 'int | str', collection_id: 'int | None' = None, exclude_unsaved: 'bool | None' = None, exclude_saved: 'bool | None' = None, exclude_unlimited: 'bool | None' = None, exclude_upgradable: 'bool | None' = None, exclude_non_upgradable: 'bool | None' = None, exclude_upgraded: 'bool | None' = None, exclude_without_colors: 'bool | None' = None, exclude_hosted: 'bool | None' = None, sort_by_price: 'bool | None' = None, limit: 'int' = 0, offset: 'str' = '') -> 'AsyncGenerator[types.Gift, None]'
```

Get all gifts owned by specified chat.

### get_chat_gifts_count

Доступен через client_call.

```python
get_chat_gifts_count(self: 'pyrogram.Client', chat_id: 'int | str') -> 'int'
```

Get the total count of owned gifts of specified chat.

### get_chat_history

Доступен через client_call.

```python
get_chat_history(self: 'pyrogram.Client', chat_id: 'int | str', limit: 'int' = 0, offset: 'int' = 0, offset_id: 'int | None' = None, offset_date: 'datetime | None' = None, min_id: 'int' = 0, max_id: 'int' = 0, reverse: 'bool' = False) -> 'AsyncGenerator[types.Message, None]'
```

Get messages from a chat history.

### get_chat_history_count

Доступен через client_call.

```python
get_chat_history_count(self: 'pyrogram.Client', chat_id: 'int | str') -> 'int'
```

Get the total count of messages in a chat.

### get_chat_invite_link

Доступен через client_call.

```python
get_chat_invite_link(self: 'pyrogram.Client', chat_id: 'int | str', invite_link: 'str') -> 'types.ChatInviteLink | None'
```

Get detailed information about a chat invite link.

### get_chat_invite_link_joiners

Доступен через client_call.

```python
get_chat_invite_link_joiners(self: 'pyrogram.Client', chat_id: 'int | str', invite_link: 'str', limit: 'int' = 0) -> 'AsyncGenerator[types.ChatJoiner, None]'
```

Get the members who joined the chat with the invite link.

### get_chat_invite_link_joiners_count

Доступен через client_call.

```python
get_chat_invite_link_joiners_count(self: 'pyrogram.Client', chat_id: 'int | str', invite_link: 'str') -> 'int'
```

Get the count of the members who joined the chat with the invite link.

### get_chat_join_requests

Доступен через client_call.

```python
get_chat_join_requests(self: 'pyrogram.Client', chat_id: 'int | str', limit: 'int' = 0, query: 'str' = '') -> 'AsyncGenerator[types.ChatJoiner, None]'
```

Get the pending join requests of a chat.

### get_chat_member

Доступен через client_call.

```python
get_chat_member(self: 'pyrogram.Client', chat_id: 'int | str', user_id: 'int | str') -> 'types.ChatMember'
```

Get information about one member of a chat.

### get_chat_members

Доступен через client_call.

```python
get_chat_members(self: 'pyrogram.Client', chat_id: 'int | str', query: 'str' = '', limit: 'int' = 0, filter: 'enums.ChatMembersFilter' = pyrogram.enums.ChatMembersFilter.SEARCH) -> 'AsyncGenerator[types.ChatMember, None]'
```

Get the members list of a chat.

### get_chat_members_count

Доступен через client_call.

```python
get_chat_members_count(self: 'pyrogram.Client', chat_id: 'int | str') -> 'int | None'
```

Get the number of members in a chat.

### get_chat_menu_button

Доступен через client_call.

```python
get_chat_menu_button(self: 'pyrogram.Client', chat_id: 'int | str | None' = None) -> 'types.MenuButton'
```

Get the current value of the bot's menu button in a private chat, or the default menu button.

### get_chat_online_count

Доступен через client_call.

```python
get_chat_online_count(self: 'pyrogram.Client', chat_id: 'int | str') -> 'int'
```

Get the number of members that are currently online in a chat.

### get_chat_photos

Доступен через client_call.

```python
get_chat_photos(self: 'pyrogram.Client', chat_id: 'int | str', limit: 'int' = 0) -> 'AsyncGenerator[types.ChatPhoto, None]'
```

Get a chat or a user profile photos sequentially.
Personal and public photo aren't returned.

### get_chat_photos_count

Доступен через client_call.

```python
get_chat_photos_count(self: 'pyrogram.Client', chat_id: 'int | str') -> 'int'
```

Get the total count of photos for a chat.

### get_chat_settings

Доступен через client_call.

```python
get_chat_settings(self: 'pyrogram.Client', chat_id: 'int | str') -> 'types.ChatSettings'
```

Get information about a chat settings.

### get_chat_stories

Доступен через client_call.

```python
get_chat_stories(self: 'pyrogram.Client', chat_id: 'int | str') -> 'AsyncGenerator[types.Story, None]'
```

Get all non expired stories from a chat by using chat identifier.

### get_chats_for_folder_invite_link

Доступен через client_call.

```python
get_chats_for_folder_invite_link(self: 'pyrogram.Client', chat_folder_id: 'int') -> 'list[types.Chat]'
```

Returns chats from a chat folder, suitable for adding to a chat folder invite link.

### get_common_chats

Доступен через client_call.

```python
get_common_chats(self: 'pyrogram.Client', user_id: 'int | str') -> 'list[types.Chat]'
```

Get the common chats you have with a user.

### get_contacts

Доступен через client_call.

```python
get_contacts(self: 'pyrogram.Client') -> 'list[types.User]'
```

Get contacts from your Telegram address book.

### get_contacts_count

Доступен через client_call.

```python
get_contacts_count(self: 'pyrogram.Client') -> 'int'
```

Get the total count of contacts from your Telegram address book.

### get_custom_emoji_stickers

Доступен через client_call.

```python
get_custom_emoji_stickers(self: 'pyrogram.Client', custom_emoji_ids: 'list[str]') -> 'list[types.Sticker]'
```

Get information about custom emoji stickers by their identifiers.

### get_dc_option

Доступен через client_call.

```python
get_dc_option(self, dc_id: 'int | None' = None, is_media: 'bool' = False, is_cdn: 'bool' = False, ipv6: 'bool' = False) -> 'raw.types.DcOption'
```



### get_default_emoji_statuses

Доступен через client_call.

```python
get_default_emoji_statuses(self: 'pyrogram.Client') -> 'list[types.EmojiStatus]'
```

Get the default emoji statuses.

### get_dialogs

Доступен через client_call.

```python
get_dialogs(self: 'pyrogram.Client', limit: 'int' = 0, exclude_pinned: 'bool | None' = None, from_archive: 'bool | None' = None) -> 'AsyncGenerator[types.Dialog, None]'
```

Get a user's dialogs sequentially.

### get_dialogs_count

Доступен через client_call.

```python
get_dialogs_count(self: 'pyrogram.Client', pinned_only: 'bool' = False, from_archive: 'bool | None' = None) -> 'int'
```

Get the total count of your dialogs.

### get_direct_messages_chat_topic_history

Доступен через client_call.

```python
get_direct_messages_chat_topic_history(self: 'pyrogram.Client', chat_id: 'int | str', topic_id: 'int', limit: 'int' = 0, offset: 'int' = 0, offset_id: 'int' = 0, offset_date: 'datetime | None' = None, min_id: 'int' = 0, max_id: 'int' = 0, reverse: 'bool' = False) -> 'AsyncGenerator[types.Message, None]'
```

Return messages in the topic in a channel direct messages chat administered by the current user.

### get_direct_messages_topics

Доступен через client_call.

```python
get_direct_messages_topics(self: 'pyrogram.Client', chat_id: 'int | str', limit: 'int' = 0, exclude_pinned: 'bool | None' = None) -> 'AsyncGenerator[types.DirectMessagesTopic, None]'
```

Get one or more topic from a direct messages channel chat.

### get_direct_messages_topics_by_id

Доступен через client_call.

```python
get_direct_messages_topics_by_id(self: 'pyrogram.Client', chat_id: 'int | str', topic_ids: 'int | Iterable[int]') -> 'types.DirectMessagesTopic | list[types.DirectMessagesTopic] | None'
```

Get one or more direct message topic from a chat by using topic identifiers.

### get_discussion_message

Доступен через client_call.

```python
get_discussion_message(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int') -> 'types.Message'
```

Get the first discussion message of a channel post or a discussion thread in a group.

### get_discussion_replies

Доступен через client_call.

```python
get_discussion_replies(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', limit: 'int' = 0) -> 'AsyncGenerator[types.Message, None]'
```

Get the message replies of a discussion thread.

### get_discussion_replies_count

Доступен через client_call.

```python
get_discussion_replies_count(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int') -> 'int'
```

Get the total count of replies in a discussion thread.

### get_file

Доступен через client_call.

```python
get_file(self, file_id: 'FileId', file_size: 'int' = 0, limit: 'int' = 0, offset: 'int' = 0, progress: 'Callable | None' = None, progress_args: 'tuple' = ()) -> 'AsyncGenerator[bytes, None]'
```



### get_folder_invite_links

Доступен через client_call.

```python
get_folder_invite_links(self: 'pyrogram.Client', chat_folder_id: 'int') -> 'list[types.FolderInviteLink]'
```

Returns invite links created by the current user for a shareable chat folder.

### get_folders

Доступен через client_call.

```python
get_folders(self: 'pyrogram.Client') -> 'list[types.Folder]'
```

Return information about a chat folders.

### get_forum_topics

Доступен через client_call.

```python
get_forum_topics(self: 'pyrogram.Client', chat_id: 'int | str', limit: 'int' = 0) -> 'AsyncGenerator[types.ForumTopic, None]'
```

Get one or more topic from a chat.

### get_forum_topics_by_id

Доступен через client_call.

```python
get_forum_topics_by_id(self: 'pyrogram.Client', chat_id: 'int | str', topic_ids: 'int | Iterable[int]') -> 'types.ForumTopic | list[types.ForumTopic]'
```

Get one or more topic from a chat by using topic identifiers.

### get_game_high_scores

Доступен через client_call.

```python
get_game_high_scores(self: 'pyrogram.Client', user_id: 'int | str', chat_id: 'int | str', message_id: 'int') -> 'list[types.GameHighScore]'
```

Get data for high score tables.

### get_gift_auction_state

Доступен через client_call.

```python
get_gift_auction_state(self: 'pyrogram.Client', auction_id: 'str | int') -> 'types.GiftAuctionState'
```

Returns auction state for a gift.

### get_gift_collections

Доступен через client_call.

```python
get_gift_collections(self: 'pyrogram.Client', owner_id: 'int | str') -> 'list[types.GiftCollection]'
```

Returns collections of gifts owned by the given user or chat.

### get_gift_upgrade_preview

Доступен через client_call.

```python
get_gift_upgrade_preview(self: 'pyrogram.Client', gift_id: 'int') -> 'types.GiftUpgradePreview'
```

Return examples of possible upgraded gifts for a regular gift.

### get_gift_upgrade_variants

Доступен через client_call.

```python
get_gift_upgrade_variants(self: 'pyrogram.Client', gift_id: 'int') -> 'types.GiftUpgradeVariants'
```

Returns all possible variants of upgraded gifts for a regular gift.

### get_gifts_for_crafting

Доступен через client_call.

```python
get_gifts_for_crafting(self: 'pyrogram.Client', regular_gift_id: 'int', limit: 'int' = 0) -> 'AsyncGenerator[types.Gift, None]'
```

Returns upgraded gifts of the current user that can be used to craft another gifts.

### get_global_privacy_settings

Доступен через client_call.

```python
get_global_privacy_settings(self: 'pyrogram.Client') -> 'types.GlobalPrivacySettings'
```

Get account global privacy settings.

### get_inline_bot_results

Доступен через client_call.

```python
get_inline_bot_results(self: 'pyrogram.Client', bot: 'int | str', query: 'str' = '', offset: 'str' = '', latitude: 'float | None' = None, longitude: 'float | None' = None) -> 'raw.base.messages.BotResults'
```

Get bot results via inline queries.
You can then send a result using :meth:`~pyrogram.Client.send_inline_bot_result`

### get_main_web_app

Доступен через client_call.

```python
get_main_web_app(self: 'pyrogram.Client', chat_id: 'int | str', bot_user_id: 'int | str', start_parameter: 'str' = '', platform: 'enums.ClientPlatform | None' = None) -> 'str'
```

Returns information needed to open the main Web App of a bot.

### get_managed_bot_access_settings

Доступен через client_call.

```python
get_managed_bot_access_settings(self: 'pyrogram.Client', user_id: 'int | str') -> 'types.BotAccessSettings'
```

Use this method to get the access settings of a managed bot.

### get_managed_bot_token

Доступен через client_call.

```python
get_managed_bot_token(self: 'pyrogram.Client', user_id: 'int | str') -> 'str'
```

Use this method to get the token of a managed bot.

### get_me

Доступен через client_call.

```python
get_me(self: 'pyrogram.Client') -> 'types.User'
```

Get your own user identity.

### get_media_group

Доступен через client_call.

```python
get_media_group(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int') -> 'list[types.Message]'
```

Get the media group a message belongs to.

### get_message_split_ranges

Доступен через client_call.

```python
get_message_split_ranges(self) -> 'list[raw.base.MessageRange]'
```



### get_messages

Доступен через client_call.

```python
get_messages(self: 'pyrogram.Client', chat_id: 'int | str | None' = None, message_ids: 'int | Iterable[int] | str | None' = None, reply: 'bool | None' = None, pinned: 'bool | None' = None, replies: 'int' = 1) -> 'types.Message | None | list[types.Message]'
```

Get one or more messages from a chat by using message identifiers or link.

### get_owned_bots

Доступен через client_call.

```python
get_owned_bots(self: 'pyrogram.Client') -> 'list[types.User]'
```

Returns the list of bots owned by the current user.

### get_password_hint

Доступен через client_call.

```python
get_password_hint(self: 'pyrogram.Client') -> 'str | None'
```

Get your Two-Step Verification password hint.

### get_payment_form

Доступен через client_call.

```python
get_payment_form(self: 'pyrogram.Client', input_invoice: 'types.InputInvoice') -> 'types.PaymentForm'
```

Get an invoice payment form.

### get_personal_channels

Доступен через client_call.

```python
get_personal_channels(self: 'pyrogram.Client') -> 'list[types.Chat] | None'
```

Get all your public channels.

### get_pinned_stories

Доступен через client_call.

```python
get_pinned_stories(self: 'pyrogram.Client', chat_id: 'int | str', offset_id: 'int' = 0, limit: 'int' = 0) -> 'AsyncGenerator[types.Story, None]'
```

Get all pinned stories from a chat by using chat identifier.

### get_privacy

Доступен через client_call.

```python
get_privacy(self: 'pyrogram.Client', key: 'enums.PrivacyKey') -> 'list[types.PrivacyRule]'
```

Get account privacy rules.

### get_received_gifts

Доступен через client_call.

```python
get_received_gifts(self: 'pyrogram.Client', chat_id: 'int | str', collection_id: 'int | None' = None, exclude_unsaved: 'bool | None' = None, exclude_saved: 'bool | None' = None, exclude_unlimited: 'bool | None' = None, exclude_upgradable: 'bool | None' = None, exclude_non_upgradable: 'bool | None' = None, exclude_upgraded: 'bool | None' = None, exclude_without_colors: 'bool | None' = None, exclude_hosted: 'bool | None' = None, sort_by_price: 'bool | None' = None, limit: 'int' = 0, offset: 'str' = '') -> 'AsyncGenerator[types.Gift, None]'
```

Get all gifts owned by specified chat.

### get_received_gifts_count

Доступен через client_call.

```python
get_received_gifts_count(self: 'pyrogram.Client', chat_id: 'int | str') -> 'int'
```

Get the total count of owned gifts of specified chat.

### get_scheduled_messages

Доступен через client_call.

```python
get_scheduled_messages(self: 'pyrogram.Client', chat_id: 'int | str') -> 'list[types.Message]'
```

Get one or more scheduled messages from a chat.

### get_send_as_chats

Доступен через client_call.

```python
get_send_as_chats(self: 'pyrogram.Client', chat_id: 'int | str', for_paid_reactions: 'bool | None' = None) -> 'list[types.Chat]'
```

Get the list of "send_as" chats available.

### get_session

Доступен через client_call.

```python
get_session(self, dc_id: 'int | None' = None, is_media: 'bool' = False, is_cdn: 'bool' = False, business_connection_id: 'str | None' = None, export_authorization: 'bool' = True, server_address: 'str | None' = None, port: 'int | None' = None, temporary: 'bool' = False) -> 'Session'
```

Get existing session or create a new one.

### get_similar_channels

Доступен через client_call.

```python
get_similar_channels(self: 'pyrogram.Client', chat_id: 'int | str') -> 'list[types.Chat] | None'
```

Get similar channels.

### get_stars_balance

Доступен через client_call.

```python
get_stars_balance(self: 'pyrogram.Client', chat_id: 'int | str | None' = None) -> 'float'
```

Get the current Telegram Stars balance of the current account.

### get_stickers

Доступен через client_call.

```python
get_stickers(self: 'pyrogram.Client', short_name: 'str') -> 'list[types.Sticker]'
```

Get all stickers from set by short name.

### get_stories

Доступен через client_call.

```python
get_stories(self: 'pyrogram.Client', chat_id: 'int | str | None' = None, story_ids: 'int | Iterable[int] | str | None' = None) -> 'types.Story | list[types.Story] | None'
```

Get one or more stories from a chat by using stories identifiers.

### get_story_views

Доступен через client_call.

```python
get_story_views(self: 'pyrogram.Client', chat_id: 'int | str', story_id: 'int', offset: 'str' = '', limit: 'int' = 0, contacts_only: 'bool | None' = None, reactions_first: 'bool | None' = None, forwards_first: 'bool | None' = None, query: 'str | None' = None) -> 'AsyncGenerator[types.StoryView, None]'
```

Obtain the list of users that have viewed a specific story we posted.

### get_suitable_discussion_chats

Доступен через client_call.

```python
get_suitable_discussion_chats(self: 'pyrogram.Client') -> 'list[types.Chat]'
```

Return a list of basic group and supergroup chats, which can be used as a discussion group for a channel.

### get_ton_balance

Доступен через client_call.

```python
get_ton_balance(self: 'pyrogram.Client') -> 'float'
```

Get the current TON balance of the current account.

### get_top_chats

Доступен через client_call.

```python
get_top_chats(self: 'pyrogram.Client', category: 'enums.TopChatCategory', limit: 'int' = 0) -> 'AsyncGenerator[types.Chat, None]'
```

Returns a list of frequently used chats.

### get_upgraded_gift

Доступен через client_call.

```python
get_upgraded_gift(self: 'pyrogram.Client', link: 'str') -> 'types.Gift'
```

Get information about upgraded gift.

### get_upgraded_gift_value_info

Доступен через client_call.

```python
get_upgraded_gift_value_info(self: 'pyrogram.Client', link: 'str') -> 'types.UpgradedGiftValueInfo'
```

Returns information about value of an upgraded gift by its name.

### get_user_personal_chat_messages

Доступен через client_call.

```python
get_user_personal_chat_messages(self: 'pyrogram.Client', user_id: 'int | str', limit: 'int' = 0, min_id: 'int' = 0, max_id: 'int' = 0) -> 'AsyncGenerator[types.Message, None]'
```

Use this method to get the last messages from the personal chat (i.e., the chat currently added to their profile) of a given user.

### get_users

Доступен через client_call.

```python
get_users(self: 'pyrogram.Client', user_ids: 'int | str | Iterable[int | str]') -> 'types.User | list[types.User] | None'
```

Get information about a user.
You can retrieve up to 200 users at once.

### get_web_app_link_url

Доступен через client_call.

```python
get_web_app_link_url(self: 'pyrogram.Client', chat_id: 'int | str', bot_user_id: 'int | str', web_app_short_name: 'str', start_parameter: 'str' = '', allow_write_access: 'bool' = False, platform: 'enums.ClientPlatform | None' = None) -> 'str'
```

Returns an HTTPS URL of a Web App to open.

### get_web_app_url

Доступен через client_call.

```python
get_web_app_url(self: 'pyrogram.Client', bot_user_id: 'int | str', url: 'str | None' = None, platform: 'enums.ClientPlatform | None' = None) -> 'str'
```

Returns an HTTPS URL of a Web App to open from the side menu,
a :obj:`~pyrogram.types.KeyboardButton` button with web app type,
or an :obj:`~pyrogram.types.InlineKeyboardButton` button with web app type.

### gift_premium_with_stars

Доступен через client_call.

```python
gift_premium_with_stars(self: 'pyrogram.Client', user_id: 'int | str', month_count: 'int', text: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, entities: 'list[types.MessageEntity] | None' = None, star_count: 'int | None' = None) -> 'types.Message | None'
```

Allows to buy a Telegram Premium subscription for another user with payment in Telegram Stars.

### guess_extension

Синхронный метод: не доступен через асинхронный client_call.

```python
guess_extension(self, mime_type: 'str') -> 'str | None'
```



### guess_mime_type

Синхронный метод: не доступен через асинхронный client_call.

```python
guess_mime_type(self, filename: 'PathType | BytesIO') -> 'str | None'
```



### handle_download

Доступен через client_call.

```python
handle_download(self, packet)
```



### handle_updates

Доступен через client_call.

```python
handle_updates(self, updates)
```



### hide_chat_stories

Доступен через client_call.

```python
hide_chat_stories(self: 'pyrogram.Client', chat_id: 'int | str') -> 'bool'
```

Hide the active stories of a user, preventing them from being displayed on the action bar on the homescreen.

### hide_gift

Доступен через client_call.

```python
hide_gift(self: 'pyrogram.Client', owned_gift_id: 'str') -> 'bool'
```

Hide gift on the current user's or the channel's profile page.

### import_contacts

Доступен через client_call.

```python
import_contacts(self: 'pyrogram.Client', contacts: 'list[types.InputPhoneContact]') -> 'raw.base.contacts.ImportedContacts'
```

Import contacts to your Telegram address book.

### increase_gift_auction_bid

Доступен через client_call.

```python
increase_gift_auction_bid(self: 'pyrogram.Client', gift_id: 'int', star_count: 'int') -> 'bool'
```

Increases a bid for an auction gift without changing gift text and receiver.

### initialize

Доступен через client_call.

```python
initialize(self: 'pyrogram.Client')
```

Initialize the client by starting up workers.

### invoke

Недоступен через client_call: исключён политикой моста.

```python
invoke(self: 'pyrogram.Client', query: 'TLObject[ReturnType]', retries: 'int' = 10, timeout: 'float' = 15, sleep_threshold: 'float | None' = None, retry_delay: 'float' = 1, recaptcha_token: 'str | None' = None, business_connection_id: 'str | None' = None) -> 'ReturnType'
```

Invoke raw Telegram functions.

### join_chat

Доступен через client_call.

```python
join_chat(self: 'pyrogram.Client', chat_id: 'int | str') -> 'types.ChatJoinResult'
```

Adds the current user as a new member to a chat. Private and secret chats can't be joined using this method.

### join_folder

Доступен через client_call.

```python
join_folder(self: 'pyrogram.Client', link: 'str') -> 'bool'
```

Join a folder by its invite link.

### leave_chat

Доступен через client_call.

```python
leave_chat(self: 'pyrogram.Client', chat_id: 'int | str', delete: 'bool' = False)
```

Leave a group chat or channel.

### leave_folder

Доступен через client_call.

```python
leave_folder(self: 'pyrogram.Client', link: 'str', keep_chats: 'bool' = True) -> 'bool'
```

Leave a folder by its invite link.

### load_plugins

Синхронный метод: не доступен через асинхронный client_call.

```python
load_plugins(self)
```



### load_session

Доступен через client_call.

```python
load_session(self)
```



### log_out

Недоступен через client_call: исключён политикой моста.

```python
log_out(self: 'pyrogram.Client') -> 'bool'
```

Log out from Telegram and delete the *\*.session* file.

### mark_chat_unread

Доступен через client_call.

```python
mark_chat_unread(self: 'pyrogram.Client', chat_id: 'int | str') -> 'bool'
```

Mark a chat as unread.

### mark_checklist_tasks_as_done

Доступен через client_call.

```python
mark_checklist_tasks_as_done(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', *, marked_as_done_task_ids: 'list[int] | None' = None, marked_as_not_done_task_ids: 'list[int] | None' = None) -> 'int'
```

Add tasks of a checklist in a message as done or not done.

### on_business_connection

Синхронный метод: не доступен через асинхронный client_call.

```python
on_business_connection(self: 'OnBusinessConnection | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling changes in business connection.

### on_business_message

Синхронный метод: не доступен через асинхронный client_call.

```python
on_business_message(self: 'OnBusinessMessage | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling new messages from business connection.

### on_callback_query

Синхронный метод: не доступен через асинхронный client_call.

```python
on_callback_query(self: 'OnCallbackQuery | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling callback queries.

### on_chat_boost

Синхронный метод: не доступен через асинхронный client_call.

```python
on_chat_boost(self: 'OnChatBoost | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling applied chat boosts.

### on_chat_join_request

Синхронный метод: не доступен через асинхронный client_call.

```python
on_chat_join_request(self: 'OnChatJoinRequest | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling chat join requests.

### on_chat_member_updated

Синхронный метод: не доступен через асинхронный client_call.

```python
on_chat_member_updated(self: 'OnChatMemberUpdated | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling event changes on chat members.

### on_chosen_inline_result

Синхронный метод: не доступен через асинхронный client_call.

```python
on_chosen_inline_result(self: 'OnChosenInlineResult | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling chosen inline results.

### on_connect

Синхронный метод: не доступен через асинхронный client_call.

```python
on_connect(self: 'OnConnect | None' = None) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling connections.

### on_deleted_business_messages

Синхронный метод: не доступен через асинхронный client_call.

```python
on_deleted_business_messages(self: 'OnDeletedBusinessMessages | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling deleted messages from business connection.

### on_deleted_messages

Синхронный метод: не доступен через асинхронный client_call.

```python
on_deleted_messages(self: 'OnDeletedMessages | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling deleted messages.

### on_disconnect

Синхронный метод: не доступен через асинхронный client_call.

```python
on_disconnect(self: 'OnDisconnect | None' = None) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling disconnections.

### on_edited_business_message

Синхронный метод: не доступен через асинхронный client_call.

```python
on_edited_business_message(self: 'OnEditedBusinessMessage | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling edited messages from business connection.

### on_edited_message

Синхронный метод: не доступен через асинхронный client_call.

```python
on_edited_message(self: 'OnEditedMessage | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling edited messages.

### on_error

Синхронный метод: не доступен через асинхронный client_call.

```python
on_error(self: 'OnError | Exception | Sequence[Exception] | None' = None, exceptions: 'Exception | Sequence[Exception] | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling unexpected errors.

### on_guest_message

Синхронный метод: не доступен через асинхронный client_call.

```python
on_guest_message(self: 'OnGuestMessage | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling new guest messages.

### on_inline_query

Синхронный метод: не доступен через асинхронный client_call.

```python
on_inline_query(self: 'OnInlineQuery | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling inline queries.

### on_managed_bot

Синхронный метод: не доступен через асинхронный client_call.

```python
on_managed_bot(self: 'OnManagedBot | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling new managed bot creation updates.

### on_message

Синхронный метод: не доступен через асинхронный client_call.

```python
on_message(self: 'OnMessage | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling new messages.

### on_message_reaction

Синхронный метод: не доступен через асинхронный client_call.

```python
on_message_reaction(self: 'OnMessageReaction | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling reaction changes on messages.

### on_message_reaction_count

Синхронный метод: не доступен через асинхронный client_call.

```python
on_message_reaction_count(self: 'OnMessageReactionCount | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling anonymous reaction changes on messages.

### on_poll

Синхронный метод: не доступен через асинхронный client_call.

```python
on_poll(self: 'OnPoll | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling poll updates.

### on_pre_checkout_query

Синхронный метод: не доступен через асинхронный client_call.

```python
on_pre_checkout_query(self: 'OnPreCheckoutQuery | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling pre-checkout queries.

### on_purchased_paid_media

Синхронный метод: не доступен через асинхронный client_call.

```python
on_purchased_paid_media(self: 'OnPurchasedPaidMedia | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling purchased paid media.

### on_raw_update

Синхронный метод: не доступен через асинхронный client_call.

```python
on_raw_update(self: 'OnRawUpdate | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling raw updates.

### on_shipping_query

Синхронный метод: не доступен через асинхронный client_call.

```python
on_shipping_query(self: 'OnShippingQuery | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling shipping queries.

### on_start

Синхронный метод: не доступен через асинхронный client_call.

```python
on_start(self: 'OnStart | None' = None) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling client start.

### on_stop

Синхронный метод: не доступен через асинхронный client_call.

```python
on_stop(self: 'OnStop | None' = None) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling client stop.

### on_stopped_message_generation

Синхронный метод: не доступен через асинхронный client_call.

```python
on_stopped_message_generation(self: 'OnStoppedMessageGeneration | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling stopped message generation.

### on_story

Синхронный метод: не доступен через асинхронный client_call.

```python
on_story(self: 'OnStory | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling new stories.

### on_user_status

Синхронный метод: не доступен через асинхронный client_call.

```python
on_user_status(self: 'OnUserStatus | Filter | None' = None, filters: 'Filter | None' = None, group: 'int' = 0) -> 'Callable[[HandlerType], HandlerType]'
```

Decorator for handling user status updates.
This does the same thing as :meth:`~pyrogram.Client.add_handler` using the
:obj:`~pyrogram.handlers.UserStatusHandler`.

### open_web_app

Доступен через client_call.

```python
open_web_app(self: 'pyrogram.Client', chat_id: 'int | str', bot_user_id: 'int | str', url: 'str | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, platform: 'enums.ClientPlatform | None' = None) -> 'str'
```

Informs pyrogram that a Web App is being opened from the attachment menu,
a :obj:`~pyrogram.types.MenuButton`, an url,
or an :obj:`~pyrogram.types.InlineKeyboardButton` button.

### pin_chat_message

Доступен через client_call.

```python
pin_chat_message(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', disable_notification: 'bool' = False, both_sides: 'bool' = False, business_connection_id: 'str | None' = None) -> 'types.Message | None'
```

Pin a message in a group, channel or your own chat.
You must be an administrator in the chat for this to work and must have the "can_pin_messages" admin right in
the supergroup or "can_edit_messages" admin right in the c

### pin_chat_stories

Доступен через client_call.

```python
pin_chat_stories(self: 'pyrogram.Client', chat_id: 'int | str', stories_ids: 'int | Iterable[int]') -> 'list[int]'
```

Pin one or more stories in a chat by using stories identifiers.

### pin_forum_topic

Доступен через client_call.

```python
pin_forum_topic(self: 'pyrogram.Client', chat_id: 'int | str', topic_id: 'int') -> 'bool'
```

Pin a forum topic.

### place_gift_auction_bid

Доступен через client_call.

```python
place_gift_auction_bid(self: 'pyrogram.Client', gift_id: 'int', star_count: 'int', user_id: 'int | str | None' = None, text: 'str | types.FormattedText | None' = None, is_private: 'bool' = False) -> 'bool'
```

Places a bid on an auction gift.

### process_chat_has_protected_content_disable_request

Доступен через client_call.

```python
process_chat_has_protected_content_disable_request(self: 'pyrogram.Client', chat_id: 'int | str', request_message_id: 'int', approve: 'bool') -> 'types.Message | bool'
```

Processes request to disable has_protected_content in a chat.

### process_gift_purchase_offer

Доступен через client_call.

```python
process_gift_purchase_offer(self: 'pyrogram.Client', message_id: 'int', accept: 'bool') -> 'types.Message | None'
```

Handles a pending gift purchase offer.

### promote_chat_member

Доступен через client_call.

```python
promote_chat_member(self: 'pyrogram.Client', chat_id: 'int | str', user_id: 'int | str', privileges: 'types.ChatAdministratorRights | None' = None) -> 'bool'
```

Promote or demote a user in a supergroup or a channel.

### read_chat_history

Доступен через client_call.

```python
read_chat_history(self: 'pyrogram.Client', chat_id: 'int | str', max_id: 'int' = 0) -> 'bool'
```

Mark a chat's message history as read.

### read_chat_stories

Доступен через client_call.

```python
read_chat_stories(self: 'pyrogram.Client', chat_id: 'int | str', max_id: 'int' = 0) -> 'list[int]'
```

Mark all stories up to a certain identifier as read, for a given chat.

### read_mentions

Доступен через client_call.

```python
read_mentions(self: 'pyrogram.Client', chat_id: 'int | str', topic_id: 'int | None' = None) -> 'bool'
```

Mark a mention in the chat as read.

### read_reactions

Доступен через client_call.

```python
read_reactions(self: 'pyrogram.Client', chat_id: 'int | str', topic_id: 'bool | None' = None) -> 'bool'
```

Mark a reaction in the chat as read.

### recover_gaps

Доступен через client_call.

```python
recover_gaps(self: 'pyrogram.Client', ids: 'int | Iterable[int] | None' = None) -> 'tuple[int, int]'
```

Restores updates for the time while the client was offline.

### recover_password

Доступен через client_call.

```python
recover_password(self: 'pyrogram.Client', recovery_code: 'str') -> 'types.User'
```

Recover your password with a recovery code and log in.

### refund_star_payment

Доступен через client_call.

```python
refund_star_payment(self: 'pyrogram.Client', user_id: 'int | str', telegram_payment_charge_id: 'str') -> 'bool'
```

Refunds a successful payment in `Telegram Stars <https://t.me/BotNews/90>`_.

### remove_cloud_password

Доступен через client_call.

```python
remove_cloud_password(self: 'pyrogram.Client', password: 'str') -> 'bool'
```

Turn off the Two-Step Verification security feature (Cloud Password) on your account.

### remove_collection_gifts

Доступен через client_call.

```python
remove_collection_gifts(self: 'pyrogram.Client', owner_id: 'int | str', collection_id: 'int', gift_ids: 'list[str]') -> 'types.GiftCollection'
```

Removes gifts from a collection.

### remove_handler

Синхронный метод: не доступен через асинхронный client_call.

```python
remove_handler(self: 'pyrogram.Client', handler: 'Handler', group: 'int' = 0)
```

Remove a previously-registered update handler.

### remove_profile_audio

Доступен через client_call.

```python
remove_profile_audio(self: 'pyrogram.Client', file_id: 'str') -> 'bool'
```

Removes an audio file from the profile audio files of the current user.

### reorder_collection_gifts

Доступен через client_call.

```python
reorder_collection_gifts(self: 'pyrogram.Client', owner_id: 'int | str', collection_id: 'int', gift_ids: 'list[str]') -> 'types.GiftCollection'
```

Changes order of gifts in a collection.

### reorder_folders

Доступен через client_call.

```python
reorder_folders(self: 'pyrogram.Client', folder_ids: 'list[int]', main_chat_list_position: 'int' = 0) -> 'bool'
```

Change the order of chat folders.

### reorder_gift_collections

Доступен через client_call.

```python
reorder_gift_collections(self: 'pyrogram.Client', owner_id: 'int | str', collection_ids: 'list[int]') -> 'types.GiftCollection'
```

Changes order of gift collections.

### replace_managed_bot_token

Доступен через client_call.

```python
replace_managed_bot_token(self: 'pyrogram.Client', user_id: 'int | str') -> 'str'
```

Use this method to revoke the current token of a managed bot and generate a new one.

### request_callback_answer

Доступен через client_call.

```python
request_callback_answer(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', callback_data: 'str | bytes', password: 'str | None' = None, timeout: 'int' = 10) -> 'raw.base.messages.BotCallbackAnswer'
```

Request a callback answer from bots.
This is the equivalent of clicking an inline button containing callback data.

### resend_code

Доступен через client_call.

```python
resend_code(self: 'pyrogram.Client', phone_number: 'str', phone_code_hash: 'str') -> 'types.SentCode'
```

Re-send the confirmation code using a different type.

### resend_phone_number_code

Доступен через client_call.

```python
resend_phone_number_code(self: 'pyrogram.Client', phone_number: 'str', phone_code_hash: 'str') -> 'types.SentCode'
```

Re-send the confirmation code using a different type.

### reset_session

Доступен через client_call.

```python
reset_session(self: 'pyrogram.Client', id: 'int') -> 'bool'
```

Log out an active authorized session by its hash.

### reset_sessions

Доступен через client_call.

```python
reset_sessions(self: 'pyrogram.Client') -> 'bool'
```

Terminates all user's authorized sessions except for the current one.

### resolve_peer

Доступен через client_call.

```python
resolve_peer(self: 'pyrogram.Client', peer_id: 'int | str') -> 'raw.base.InputPeer | None'
```

Get the InputPeer of a known peer id. Useful whenever an InputPeer type is required.

### restart

Доступен через client_call.

```python
restart(self: 'pyrogram.Client', block: 'bool' = True, clear_handlers: 'bool' = False) -> 'pyrogram.Client'
```

Restart the Client.

### restrict_chat_member

Доступен через client_call.

```python
restrict_chat_member(self: 'pyrogram.Client', chat_id: 'int | str', user_id: 'int | str', permissions: 'types.ChatPermissions', until_date: 'datetime | None' = None) -> 'types.Chat'
```

Restrict a user in a supergroup.

### retract_vote

Доступен через client_call.

```python
retract_vote(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int') -> 'types.Poll'
```

Retract your vote in a poll.

### reuse_star_subscription

Доступен через client_call.

```python
reuse_star_subscription(self: 'pyrogram.Client', subscription_id: 'str') -> 'bool'
```

Reuses an active Telegram Star subscription to a channel chat and joins the chat again.

### revoke_chat_invite_link

Доступен через client_call.

```python
revoke_chat_invite_link(self: 'pyrogram.Client', chat_id: 'int | str', invite_link: 'str') -> 'types.ChatInviteLink | None'
```

Revoke a previously created invite link.

### run

Недоступен через client_call: исключён политикой моста.

```python
run(self: 'pyrogram.Client', *, use_qr: 'bool' = False, except_ids: 'list[int] | None' = None)
```

Start the client, idle the main script and finally stop the client.

### save_file

Доступен через client_call.

```python
save_file(self: 'pyrogram.Client', path: 'PathType | BinaryIO | None', file_id: 'int | None' = None, file_part: 'int' = 0, progress: 'Callable | None' = None, progress_args: 'tuple' = ()) -> 'raw.types.InputFile | raw.types.InputFileBig | None'
```

Upload a file onto Telegram servers, without actually sending the message to anyone.
Useful whenever an InputFile type is required.

### search_contacts

Доступен через client_call.

```python
search_contacts(self: 'pyrogram.Client', query: 'str', limit: 'int' = 0) -> 'types.FoundContacts'
```

Returns users or channels found by name substring and auxiliary data.

### search_gifts_for_resale

Доступен через client_call.

```python
search_gifts_for_resale(self: 'pyrogram.Client', gift_id: 'int', order: 'enums.GiftForResaleOrder' = pyrogram.enums.GiftForResaleOrder.CHANGE_DATE, for_crafting: 'bool | None' = None, for_stars: 'bool | None' = None, attributes: 'list[types.UpgradedGiftAttributeId] | None' = None, limit: 'int' = 0, offset: 'str' = '') -> 'AsyncGenerator[types.Gift, None]'
```

Get upgraded gifts that can be bought from other owners.

### search_global

Доступен через client_call.

```python
search_global(self: 'pyrogram.Client', query: 'str' = '', filter: 'enums.MessagesFilter' = pyrogram.enums.MessagesFilter.EMPTY, channels_only: 'bool | None' = None, groups_only: 'bool | None' = None, users_only: 'bool | None' = None, limit: 'int' = 0) -> 'AsyncGenerator[types.Message, None]'
```

Search messages globally from all of your chats.

### search_global_count

Доступен через client_call.

```python
search_global_count(self: 'pyrogram.Client', query: 'str' = '', filter: 'enums.MessagesFilter' = pyrogram.enums.MessagesFilter.EMPTY, channels_only: 'bool | None' = None, groups_only: 'bool | None' = None, users_only: 'bool | None' = None) -> 'int'
```

Get the count of messages resulting from a global search.

### search_messages

Доступен через client_call.

```python
search_messages(self: 'pyrogram.Client', chat_id: 'int | str', query: 'str' = '', offset: 'int' = 0, offset_id: 'int' = 0, min_date: 'datetime | None' = None, max_date: 'datetime | None' = None, min_id: 'int' = 0, max_id: 'int' = 0, filter: 'enums.MessagesFilter' = pyrogram.enums.MessagesFilter.EMPTY, limit: 'int' = 0, from_user: 'int | str | None' = None, message_thread_id: 'int | None' = None) -> 'AsyncGenerator[types.Message, None]'
```

Search for text and media messages inside a specific chat.

### search_messages_count

Доступен через client_call.

```python
search_messages_count(self: 'pyrogram.Client', chat_id: 'int | str', query: 'str' = '', filter: 'enums.MessagesFilter' = pyrogram.enums.MessagesFilter.EMPTY, from_user: 'int | str | None' = None, message_thread_id: 'int | None' = None) -> 'int'
```

Get the count of messages resulting from a search inside a chat.

### search_posts

Доступен через client_call.

```python
search_posts(self: 'pyrogram.Client', hashtag: 'str', limit: 'int' = 0) -> 'AsyncGenerator[types.Message, None]'
```

Search posts globally by hashtag.

### search_posts_count

Доступен через client_call.

```python
search_posts_count(self: 'pyrogram.Client', hashtag: 'str') -> 'int'
```

Get the count of posts with hashtag resulting from a search.

### send_animation

Доступен через client_call.

```python
send_animation(self: 'pyrogram.Client', chat_id: 'int | str', animation: 'PathType | BinaryIO', caption: 'str' = '', unsave: 'bool' = False, parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None, has_spoiler: 'bool | None' = None, duration: 'int' = 0, width: 'int' = 0, height: 'int' = 0, thumb: 'PathType | BinaryIO | None' = None, file_name: 'str | None' = None, disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, ephemeral_message_parameters: 'types.EphemeralMessageParameters | None' = None, effect_id: 'int | None' = None, show_caption_above_media: 'bool | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, schedule_date: 'datetime | None' = None, repeat_period: 'int | None' = None, protect_content: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, progress: 'Callable | None' = None, progress_args: 'tuple' = (), reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, reply_to_story_id: 'int | None' = None, quote_text: 'str | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'types.Message | None'
```

Send animation files (animation or H.264/MPEG-4 AVC video without sound).

### send_audio

Доступен через client_call.

```python
send_audio(self: 'pyrogram.Client', chat_id: 'int | str', audio: 'PathType | BinaryIO', caption: 'str' = '', parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None, duration: 'int' = 0, performer: 'str | None' = None, title: 'str | None' = None, thumb: 'PathType | BinaryIO | None' = None, file_name: 'str | None' = None, disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, ephemeral_message_parameters: 'types.EphemeralMessageParameters | None' = None, effect_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, schedule_date: 'datetime | None' = None, repeat_period: 'int | None' = None, protect_content: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, progress: 'Callable | None' = None, progress_args: 'tuple' = (), reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, reply_to_story_id: 'int | None' = None, quote_text: 'str | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'types.Message | None'
```

Send audio files.

### send_cached_media

Доступен через client_call.

```python
send_cached_media(self: 'pyrogram.Client', chat_id: 'int | str', file_id: 'str', caption: 'str' = '', parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None, disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, schedule_date: 'datetime | None' = None, protect_content: 'bool | None' = None, has_spoiler: 'bool | None' = None, effect_id: 'int | None' = None, show_caption_above_media: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, reply_to_story_id: 'int | None' = None, quote_text: 'str | None' = None, quote_offset: 'int | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None) -> 'types.Message | None'
```

Send any media stored on the Telegram servers using a file_id.

### send_chat_action

Доступен через client_call.

```python
send_chat_action(self: 'pyrogram.Client', chat_id: 'int | str', action: 'enums.ChatAction', business_connection_id: 'str | None' = None) -> 'bool'
```

Tell the other party that something is happening on your side.

### send_chat_join_request_web_app

Доступен через client_call.

```python
send_chat_join_request_web_app(self: 'pyrogram.Client', chat_join_request_query_id: 'str', web_app_url: 'str') -> 'bool'
```

Use this method to process a received chat join request query by showing a Mini App to the user before deciding the outcome.
Call :meth:`~pyrogram.Client.answer_chat_join_request_query` to resolve the join request query

### send_checklist

Доступен через client_call.

```python
send_checklist(self: 'pyrogram.Client', chat_id: 'int | str', checklist: 'types.InputChecklist', disable_notification: 'bool | None' = None, protect_content: 'bool | None' = None, message_thread_id: 'int | None' = None, effect_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, schedule_date: 'datetime | None' = None, repeat_period: 'int | None' = None, business_connection_id: 'str | None' = None, paid_message_star_count: 'int | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None) -> 'types.Message | None'
```

Send a new checklist.

### send_code

Недоступен через client_call: исключён политикой моста.

```python
send_code(self: 'pyrogram.Client', phone_number: 'str', settings: 'types.PhoneNumberAuthenticationSettings | None' = None, type: 'enums.PhoneNumberCodeType' = pyrogram.enums.PhoneNumberCodeType.AUTHENTICATION, recaptcha_token: 'str | None' = None, current_number: 'bool | None' = None, allow_flashcall: 'bool | None' = None, allow_app_hash: 'bool | None' = None, allow_missed_call: 'bool | None' = None, allow_firebase: 'bool | None' = None, logout_tokens: 'list[bytes] | None' = None, token: 'str | None' = None, app_sandbox: 'bool | None' = None) -> 'types.SentCode'
```

Sends a code to the specified phone number. Aborts previous phone number verification if there was one.

### send_contact

Доступен через client_call.

```python
send_contact(self: 'pyrogram.Client', chat_id: 'int | str', phone_number: 'str', first_name: 'str', last_name: 'str | None' = None, vcard: 'str | None' = None, disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, ephemeral_message_parameters: 'types.EphemeralMessageParameters | None' = None, effect_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, schedule_date: 'datetime | None' = None, protect_content: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, quote_text: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'types.Message | None'
```

Send phone contacts.

### send_dice

Доступен через client_call.

```python
send_dice(self: 'pyrogram.Client', chat_id: 'int | str', emoji: 'str' = '🎲', disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, effect_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, schedule_date: 'datetime | None' = None, protect_content: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, reply_to_story_id: 'int | None' = None, quote_text: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'types.Message | None'
```

Send a dice with a random value from 1 to 6.

### send_document

Доступен через client_call.

```python
send_document(self: 'pyrogram.Client', chat_id: 'int | str', document: 'PathType | BinaryIO', thumb: 'PathType | BinaryIO | None' = None, caption: 'str' = '', parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None, file_name: 'str | None' = None, force_document: 'bool | None' = None, disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, ephemeral_message_parameters: 'types.EphemeralMessageParameters | None' = None, effect_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, schedule_date: 'datetime | None' = None, repeat_period: 'int | None' = None, protect_content: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, progress: 'Callable | None' = None, progress_args: 'tuple' = (), reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, reply_to_story_id: 'int | None' = None, quote_text: 'str | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'types.Message | None'
```

Send generic files.

### send_game

Доступен через client_call.

```python
send_game(self: 'pyrogram.Client', chat_id: 'int | str', game_short_name: 'str', disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, effect_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, protect_content: 'bool | None' = None, allow_paid_broadcast: 'bool | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None) -> 'types.Message | None'
```

Send a game.

### send_gift

Доступен через client_call.

```python
send_gift(self: 'pyrogram.Client', chat_id: 'int | str', gift_id: 'int', text: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, entities: 'list[types.MessageEntity] | None' = None, is_private: 'bool | None' = None, pay_for_upgrade: 'bool | None' = None) -> 'types.Message | None'
```

Send a gift to another user or channel chat. May return an error with a message "STARGIFT_USAGE_LIMITED" if the gift was sold out.

### send_gift_purchase_offer

Доступен через client_call.

```python
send_gift_purchase_offer(self: 'pyrogram.Client', owner_id: 'int | str', gift_name: 'str', price: 'types.GiftResalePrice', duration: 'int', paid_message_star_count: 'int | None' = None) -> 'types.Message | None'
```

Sends an offer to purchase an upgraded gift.

### send_inline_bot_result

Доступен через client_call.

```python
send_inline_bot_result(self: 'pyrogram.Client', chat_id: 'int | str', query_id: 'int', result_id: 'str', disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, paid_message_star_count: 'int | None' = None, schedule_date: 'datetime | None' = None, reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, reply_to_story_id: 'int | None' = None, quote_text: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'types.Message | None'
```

Send an inline bot result.
Bot results can be retrieved using :meth:`~pyrogram.Client.get_inline_bot_results`

### send_invoice

Доступен через client_call.

```python
send_invoice(self: 'pyrogram.Client', chat_id: 'int | str', title: 'str', description: 'str', payload: 'str | bytes', currency: 'str', prices: 'list[types.LabeledPrice]', message_thread_id: 'int | None' = None, provider_token: 'str | None' = None, max_tip_amount: 'int | None' = None, suggested_tip_amounts: 'list[int] | None' = None, start_parameter: 'str | None' = None, provider_data: 'str | None' = None, photo_url: 'str | None' = None, photo_size: 'int | None' = None, photo_width: 'int | None' = None, photo_height: 'int | None' = None, need_name: 'bool | None' = None, need_phone_number: 'bool | None' = None, need_email: 'bool | None' = None, need_shipping_address: 'bool | None' = None, send_phone_number_to_provider: 'bool | None' = None, send_email_to_provider: 'bool | None' = None, is_flexible: 'bool | None' = None, disable_notification: 'bool | None' = None, protect_content: 'bool | None' = None, message_effect_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, allow_paid_broadcast: 'bool | None' = None, direct_messages_topic_id: 'int | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, subscription_expiration_date: 'int | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, caption: 'str' = '', parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None, reply_to_message_id: 'int | None' = None) -> 'types.Message | None'
```

Use this method to send invoices.

### send_live_photo

Доступен через client_call.

```python
send_live_photo(self: 'pyrogram.Client', chat_id: 'int | str', live_photo: 'PathType | BinaryIO', photo: 'PathType | BinaryIO', caption: 'str' = '', parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None, has_spoiler: 'bool | None' = None, width: 'int' = 0, height: 'int' = 0, disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, ephemeral_message_parameters: 'types.EphemeralMessageParameters | None' = None, effect_id: 'int | None' = None, show_caption_above_media: 'bool | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, schedule_date: 'datetime | None' = None, repeat_period: 'int | None' = None, protect_content: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, progress: 'Callable | None' = None, progress_args: 'tuple' = ()) -> 'types.Message | None'
```

Send video files.

### send_location

Доступен через client_call.

```python
send_location(self: 'pyrogram.Client', chat_id: 'int | str', latitude: 'float', longitude: 'float', horizontal_accuracy: 'float | None' = None, live_period: 'int | None' = None, heading: 'int | None' = None, proximity_alert_radius: 'int | None' = None, disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, ephemeral_message_parameters: 'types.EphemeralMessageParameters | None' = None, effect_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, schedule_date: 'datetime | None' = None, protect_content: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, quote_text: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'types.Message | None'
```

Send points on the map.

### send_media_group

Доступен через client_call.

```python
send_media_group(self: 'pyrogram.Client', chat_id: 'int | str', media: 'list[types.InputMediaPhoto | types.InputMediaVideo | types.InputMediaAudio | types.InputMediaDocument]', disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, effect_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, schedule_date: 'datetime | None' = None, protect_content: 'bool | None' = None, show_caption_above_media: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, reply_to_story_id: 'int | None' = None, quote_text: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'list[types.Message]'
```

Send a group of photos or videos as an album.

### send_message

Доступен через client_call.

```python
send_message(self: 'pyrogram.Client', chat_id: 'int | str', text: 'str', parse_mode: 'enums.ParseMode | None' = None, entities: 'list[types.MessageEntity] | None' = None, link_preview_options: 'types.LinkPreviewOptions | None' = None, disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, ephemeral_message_parameters: 'types.EphemeralMessageParameters | None' = None, effect_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, schedule_date: 'datetime | None' = None, repeat_period: 'int | None' = None, protect_content: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, show_caption_above_media: 'bool | None' = None, reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, reply_to_story_id: 'int | None' = None, quote_text: 'str | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None, disable_web_page_preview: 'bool | None' = None) -> 'types.Message | None'
```

Send text messages.

### send_message_draft

Доступен через client_call.

```python
send_message_draft(self: 'pyrogram.Client', chat_id: 'int | str', draft_id: 'int', text: 'str' = '', message_thread_id: 'int | None' = None, parse_mode: 'enums.ParseMode | None' = None, entities: 'list[types.MessageEntity] | None' = None, can_stop: 'bool | None' = None, keep_on_stop: 'bool | None' = None) -> 'bool'
```

Use this method to stream a partial message to a user while the message is being generated.

### send_paid_media

Доступен через client_call.

```python
send_paid_media(self: 'pyrogram.Client', chat_id: 'int | str', stars_amount: 'int', media: 'list[types.InputMediaPhoto | types.InputMediaVideo]', caption: 'str' = '', payload: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None, disable_notification: 'bool | None' = None, direct_messages_topic_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, schedule_date: 'datetime | None' = None, protect_content: 'bool | None' = None, show_caption_above_media: 'bool | None' = None, business_connection_id: 'str | None' = None, reply_to_message_id: 'int | None' = None, quote_text: 'str | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'list[types.Message]'
```

Send a group or one paid photo/video.

### send_paid_reaction

Доступен через client_call.

```python
send_paid_reaction(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', amount: 'int', privacy: 'enums.PaidReactionPrivacy | None' = None, send_as: 'int | str | None' = None) -> 'bool'
```

Send a paid reaction to a message.

### send_payment_form

Доступен через client_call.

```python
send_payment_form(self: 'pyrogram.Client', payment_form_id: 'int', input_invoice: 'types.InputInvoice', credentials: 'types.InputCredentials | None' = None) -> 'types.PaymentResult'
```

Send a filled-out payment form to the bot for final verification.

### send_phone_number_code

Доступен через client_call.

```python
send_phone_number_code(self: 'pyrogram.Client', phone_number: 'str', settings: 'types.PhoneNumberAuthenticationSettings | None' = None, type: 'enums.PhoneNumberCodeType' = pyrogram.enums.PhoneNumberCodeType.AUTHENTICATION, recaptcha_token: 'str | None' = None, current_number: 'bool | None' = None, allow_flashcall: 'bool | None' = None, allow_app_hash: 'bool | None' = None, allow_missed_call: 'bool | None' = None, allow_firebase: 'bool | None' = None, logout_tokens: 'list[bytes] | None' = None, token: 'str | None' = None, app_sandbox: 'bool | None' = None) -> 'types.SentCode'
```

Sends a code to the specified phone number. Aborts previous phone number verification if there was one.

### send_photo

Доступен через client_call.

```python
send_photo(self: 'pyrogram.Client', chat_id: 'int | str', photo: 'PathType | BinaryIO', caption: 'str' = '', parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None, has_spoiler: 'bool | None' = None, ttl_seconds: 'int | None' = None, disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, ephemeral_message_parameters: 'types.EphemeralMessageParameters | None' = None, effect_id: 'int | None' = None, show_caption_above_media: 'bool | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, schedule_date: 'datetime | None' = None, repeat_period: 'int | None' = None, protect_content: 'bool | None' = None, view_once: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, progress: 'Callable | None' = None, progress_args: 'tuple' = (), reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, reply_to_story_id: 'int | None' = None, quote_text: 'str | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'types.Message | None'
```

Send photos.

### send_poll

Доступен через client_call.

```python
send_poll(self: 'pyrogram.Client', chat_id: 'int | str', question: 'str | types.FormattedText', options: 'list[str | types.InputPollOption]', description: 'str | types.FormattedText | None' = None, description_media: 'types.InputPollMedia | None' = None, message_thread_id: 'int | None' = None, business_connection_id: 'str | None' = None, is_anonymous: 'bool' = True, type: 'enums.PollType' = pyrogram.enums.PollType.REGULAR, allows_multiple_answers: 'bool | None' = None, allows_revoting: 'bool | None' = None, members_only: 'bool | None' = None, country_codes: 'list[str] | None' = None, shuffle_options: 'bool | None' = None, allow_adding_options: 'bool | None' = None, hide_results_until_closes: 'bool | None' = None, correct_option_ids: 'list[int] | None' = None, explanation: 'str | types.FormattedText | None' = None, explanation_media: 'types.InputPollMedia | None' = None, open_period: 'int | None' = None, close_date: 'datetime | None' = None, is_closed: 'bool | None' = None, disable_notification: 'bool | None' = None, protect_content: 'bool | None' = None, allow_paid_broadcast: 'bool | None' = None, effect_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, schedule_date: 'datetime | None' = None, repeat_period: 'int | None' = None, paid_message_star_count: 'int | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None) -> 'types.Message | None'
```

A message with a poll.

### send_reaction

Доступен через client_call.

```python
send_reaction(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int | None' = None, emoji: 'int | str | list[int | str] | None' = None, story_id: 'int | None' = None, big: 'bool' = False, business_connection_id: 'str | None' = None) -> 'bool'
```

Send a reaction to a message or story.

### send_recovery_code

Доступен через client_call.

```python
send_recovery_code(self: 'pyrogram.Client') -> 'str'
```

Send a code to your email to recover your password.

### send_resold_gift

Доступен через client_call.

```python
send_resold_gift(self: 'pyrogram.Client', gift_link: 'str', new_owner_chat_id: 'int | str', price: 'types.GiftResalePrice') -> 'types.Message | None'
```

Send an upgraded gift that is available for resale to another user or channel chat.

### send_rich_message

Доступен через client_call.

```python
send_rich_message(self: 'pyrogram.Client', chat_id: 'int | str', rich_message: 'types.InputRichMessage', disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, ephemeral_message_parameters: 'types.EphemeralMessageParameters | None' = None, effect_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, protect_content: 'bool | None' = None, allow_paid_broadcast: 'bool | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None) -> 'types.Message | None'
```

Send text messages.

### send_rich_message_draft

Доступен через client_call.

```python
send_rich_message_draft(self: 'pyrogram.Client', chat_id: 'int | str', draft_id: 'int', rich_message: 'types.InputRichMessage', message_thread_id: 'int | None' = None, can_stop: 'bool | None' = None, keep_on_stop: 'bool | None' = None) -> 'bool'
```

Use this method to stream a partial rich message to a user while the message is being generated.

### send_screenshot_notification

Доступен через client_call.

```python
send_screenshot_notification(self: 'pyrogram.Client', chat_id: 'int | str', reply_parameters: 'types.ReplyParameters | None' = None) -> 'types.Message | None'
```

Notify the other user in a private chat that a screenshot of the chat was taken.

### send_sticker

Доступен через client_call.

```python
send_sticker(self: 'pyrogram.Client', chat_id: 'int | str', sticker: 'PathType | BinaryIO', emoji: 'str' = '', caption: 'str' = '', parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None, disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, ephemeral_message_parameters: 'types.EphemeralMessageParameters | None' = None, effect_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, schedule_date: 'datetime | None' = None, repeat_period: 'int | None' = None, protect_content: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, progress: 'Callable | None' = None, progress_args: 'tuple' = (), reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, reply_to_story_id: 'int | None' = None, quote_text: 'str | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'types.Message | None'
```

Send static .webp or animated .tgs stickers.

### send_story

Доступен через client_call.

```python
send_story(self: 'pyrogram.Client', chat_id: 'int | str', media: 'PathType | BinaryIO', caption: 'str | None' = None, period: 'int | None' = None, media_areas: 'list[types.MediaArea] | None' = None, duration: 'int' = 0, width: 'int' = 0, height: 'int' = 0, thumb: 'PathType | BinaryIO | None' = None, supports_streaming: 'bool' = True, file_name: 'str | None' = None, privacy: 'enums.StoriesPrivacyRules | None' = None, allowed_users: 'list[int | str] | None' = None, disallowed_users: 'list[int | str] | None' = None, pinned: 'bool | None' = None, protect_content: 'bool | None' = None, parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None, progress: 'Callable | None' = None, progress_args: 'tuple' = ()) -> 'types.Story | None'
```

Post new story.

### send_venue

Доступен через client_call.

```python
send_venue(self: 'pyrogram.Client', chat_id: 'int | str', latitude: 'float', longitude: 'float', title: 'str', address: 'str', foursquare_id: 'str' = '', foursquare_type: 'str' = '', disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, ephemeral_message_parameters: 'types.EphemeralMessageParameters | None' = None, effect_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, schedule_date: 'datetime | None' = None, protect_content: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, quote_text: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'types.Message | None'
```

Send information about a venue.

### send_video

Доступен через client_call.

```python
send_video(self: 'pyrogram.Client', chat_id: 'int | str', video: 'PathType | BinaryIO', caption: 'str' = '', parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None, has_spoiler: 'bool | None' = None, ttl_seconds: 'int | None' = None, view_once: 'bool | None' = None, duration: 'int' = 0, width: 'int' = 0, height: 'int' = 0, video_start_timestamp: 'int | None' = None, video_cover: 'PathType | BinaryIO | None' = None, thumb: 'PathType | BinaryIO | None' = None, file_name: 'str | None' = None, supports_streaming: 'bool' = True, disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, ephemeral_message_parameters: 'types.EphemeralMessageParameters | None' = None, effect_id: 'int | None' = None, show_caption_above_media: 'bool | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, schedule_date: 'datetime | None' = None, repeat_period: 'int | None' = None, protect_content: 'bool | None' = None, no_sound: 'bool' = True, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, progress: 'Callable | None' = None, progress_args: 'tuple' = (), reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, reply_to_story_id: 'int | None' = None, quote_text: 'str | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'types.Message | None'
```

Send video files.

### send_video_note

Доступен через client_call.

```python
send_video_note(self: 'pyrogram.Client', chat_id: 'int | str', video_note: 'PathType | BinaryIO', duration: 'int' = 0, length: 'int' = 1, thumb: 'PathType | BinaryIO | None' = None, disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, ephemeral_message_parameters: 'types.EphemeralMessageParameters | None' = None, effect_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, schedule_date: 'datetime | None' = None, repeat_period: 'int | None' = None, protect_content: 'bool | None' = None, view_once: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, progress: 'Callable | None' = None, progress_args: 'tuple' = (), reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, reply_to_story_id: 'int | None' = None, quote_text: 'str | None' = None, parse_mode: 'enums.ParseMode | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'types.Message | None'
```

Send video messages.

### send_voice

Доступен через client_call.

```python
send_voice(self: 'pyrogram.Client', chat_id: 'int | str', voice: 'PathType | BinaryIO', caption: 'str' = '', parse_mode: 'enums.ParseMode | None' = None, caption_entities: 'list[types.MessageEntity] | None' = None, duration: 'int' = 0, waveform: 'bytes | None' = None, disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, ephemeral_message_parameters: 'types.EphemeralMessageParameters | None' = None, effect_id: 'int | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, schedule_date: 'datetime | None' = None, repeat_period: 'int | None' = None, protect_content: 'bool | None' = None, view_once: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, suggested_post_parameters: 'types.SuggestedPostParameters | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, progress: 'Callable | None' = None, progress_args: 'tuple' = (), reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, reply_to_story_id: 'int | None' = None, quote_text: 'str | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'types.Message | None'
```

Send audio files.

### send_web_page

Доступен через client_call.

```python
send_web_page(self: 'pyrogram.Client', chat_id: 'int | str', text: 'str' = '', url: 'str | None' = None, prefer_large_media: 'bool | None' = None, prefer_small_media: 'bool | None' = None, parse_mode: 'enums.ParseMode | None' = None, entities: 'list[types.MessageEntity] | None' = None, link_preview_options: 'types.LinkPreviewOptions | None' = None, disable_notification: 'bool | None' = None, message_thread_id: 'int | None' = None, direct_messages_topic_id: 'int | None' = None, effect_id: 'int | None' = None, show_caption_above_media: 'bool | None' = None, reply_parameters: 'types.ReplyParameters | None' = None, schedule_date: 'datetime | None' = None, repeat_period: 'int | None' = None, protect_content: 'bool | None' = None, business_connection_id: 'str | None' = None, allow_paid_broadcast: 'bool | None' = None, paid_message_star_count: 'int | None' = None, reply_markup: 'types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | None' = None, reply_to_message_id: 'int | None' = None, reply_to_chat_id: 'int | str | None' = None, reply_to_story_id: 'int | None' = None, quote_text: 'str | None' = None, quote_entities: 'list[types.MessageEntity] | None' = None, quote_offset: 'int | None' = None) -> 'types.Message | None'
```

Send Web Page Preview.

### set_account_ttl

Доступен через client_call.

```python
set_account_ttl(self: 'pyrogram.Client', days: 'int') -> 'bool'
```

Set days to live of account.

### set_administrator_title

Доступен через client_call.

```python
set_administrator_title(self: 'pyrogram.Client', chat_id: 'int | str', user_id: 'int | str', title: 'str') -> 'bool'
```

Set a custom title (rank) to an administrator of a supergroup.

### set_bot_commands

Доступен через client_call.

```python
set_bot_commands(self: 'pyrogram.Client', commands: 'list[types.BotCommand]', scope: 'types.BotCommandScope | None' = None, language_code: 'str' = '') -> 'bool'
```

Set the list of the bot's commands.
The commands passed will overwrite any command set previously.
This method can be used by the own bot only.

### set_bot_default_privileges

Доступен через client_call.

```python
set_bot_default_privileges(self: 'pyrogram.Client', privileges: 'types.ChatAdministratorRights | None' = None, for_channels: 'bool | None' = None) -> 'bool'
```

Change the default privileges requested by the bot when it's added as an administrator to groups or channels.

### set_bot_info_description

Доступен через client_call.

```python
set_bot_info_description(self: 'pyrogram.Client', description: 'str', language_code: 'str' = '', for_my_bot: 'int | str | None' = None) -> 'bool'
```

Use this method to change the bot's description, which is shown in the chat with the bot if the chat is empty.

### set_bot_info_short_description

Доступен через client_call.

```python
set_bot_info_short_description(self: 'pyrogram.Client', short_description: 'str', language_code: 'str' = '', for_my_bot: 'int | str | None' = None) -> 'bool'
```

Use this method to change the bot's short description, which is shown on the bot's profile page and is sent together with the link when users share the bot.

### set_bot_name

Доступен через client_call.

```python
set_bot_name(self: 'pyrogram.Client', name: 'str', language_code: 'str' = '', for_my_bot: 'int | str | None' = None) -> 'str'
```

Use this method to get the current / owned bot name for the given user language.

### set_chat_accent_color

Доступен через client_call.

```python
set_chat_accent_color(self: 'pyrogram.Client', chat_id: 'int | str', accent_color_id: 'int | None' = None, background_custom_emoji_id: 'str | None' = None) -> 'bool'
```

Update color

### set_chat_description

Доступен через client_call.

```python
set_chat_description(self: 'pyrogram.Client', chat_id: 'int | str', description: 'str') -> 'bool'
```

Change the description of a supergroup or a channel.
You must be an administrator in the chat for this to work and must have the appropriate admin rights.

### set_chat_direct_messages_group

Доступен через client_call.

```python
set_chat_direct_messages_group(self: 'pyrogram.Client', chat_id: 'int | str', paid_message_star_count: 'int' = 0, is_enabled: 'bool | None' = None) -> 'bool'
```

Change direct messages group settings for a channel chat.

### set_chat_discussion_group

Доступен через client_call.

```python
set_chat_discussion_group(self: 'pyrogram.Client', *, chat_id: 'int | str | None' = None, discussion_chat_id: 'int | str | None' = None) -> 'bool'
```

Change the discussion group of a channel chat.

### set_chat_member_tag

Доступен через client_call.

```python
set_chat_member_tag(self: 'pyrogram.Client', chat_id: 'int | str', user_id: 'int | str', tag: 'str | None' = None) -> 'bool'
```

Use this method to set a tag for a regular member in a group or a supergroup.

### set_chat_menu_button

Доступен через client_call.

```python
set_chat_menu_button(self: 'pyrogram.Client', chat_id: 'int | str | None' = None, menu_button: 'types.MenuButton | None' = None) -> 'bool'
```

Change the bot's menu button in a private chat, or the default menu button.

### set_chat_permissions

Доступен через client_call.

```python
set_chat_permissions(self: 'pyrogram.Client', chat_id: 'int | str', permissions: 'types.ChatPermissions | None' = None) -> 'types.Chat'
```

Set default chat permissions for all members.

### set_chat_photo

Доступен через client_call.

```python
set_chat_photo(self: 'pyrogram.Client', chat_id: 'int | str', *, photo: 'PathType | BinaryIO | None' = None, video: 'PathType | BinaryIO | None' = None, video_start_ts: 'float | None' = None) -> 'types.Message | None'
```

Set a new chat photo or video (H.264/MPEG-4 AVC video, max 5 seconds).

### set_chat_profile_accent_color

Доступен через client_call.

```python
set_chat_profile_accent_color(self: 'pyrogram.Client', chat_id: 'int | str', profile_accent_color_id: 'int | None' = None, profile_background_custom_emoji_id: 'str | None' = None) -> 'bool'
```

Update color

### set_chat_protected_content

Доступен через client_call.

```python
set_chat_protected_content(self: 'pyrogram.Client', chat_id: 'int | str', enabled: 'bool') -> 'types.Message | bool'
```

Set the chat protected content setting.

### set_chat_title

Доступен через client_call.

```python
set_chat_title(self: 'pyrogram.Client', chat_id: 'int | str', title: 'str') -> 'types.Message | None'
```

Change the title of a chat.

### set_chat_ttl

Доступен через client_call.

```python
set_chat_ttl(self: 'pyrogram.Client', chat_id: 'int | str', ttl_seconds: 'int') -> 'types.Message | None'
```

Set the time-to-live for the chat.

### set_chat_username

Доступен через client_call.

```python
set_chat_username(self: 'pyrogram.Client', chat_id: 'int | str', username: 'str | None') -> 'bool'
```

Set a channel or a supergroup username.

### set_contact_note

Доступен через client_call.

```python
set_contact_note(self: 'pyrogram.Client', user_id: 'int | str', note: 'str | types.FormattedText | None' = None) -> 'bool'
```

Changes a note of a contact user.

### set_dc

Доступен через client_call.

```python
set_dc(self, dc_id: 'int | None' = None, server_address: 'str | None' = None, port: 'int | None' = None)
```

Set configuration for the specified datacenter.

### set_direct_messages_chat_topic_is_marked_as_unread

Доступен через client_call.

```python
set_direct_messages_chat_topic_is_marked_as_unread(self: 'pyrogram.Client', chat_id: 'int | str', topic_id: 'int', is_marked_as_unread: 'bool' = True) -> 'int'
```

Change the marked as unread state of the topic in a channel direct messages chat administered by the current user.

### set_emoji_status

Доступен через client_call.

```python
set_emoji_status(self: 'pyrogram.Client', chat_id: 'int | str | None' = None, emoji_status: 'types.EmojiStatus | None' = None) -> 'bool'
```

Set the emoji status.

### set_game_score

Доступен через client_call.

```python
set_game_score(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', user_id: 'int | str', score: 'int', force: 'bool | None' = None, disable_edit_message: 'bool | None' = None) -> 'types.Message | bool'
```

Set the score of the specified user in a game.

### set_gift_collection_name

Доступен через client_call.

```python
set_gift_collection_name(self: 'pyrogram.Client', owner_id: 'int | str', collection_id: 'int', name: 'str') -> 'types.GiftCollection'
```

Changes name of a gift collection.

### set_gift_resale_price

Доступен через client_call.

```python
set_gift_resale_price(self: 'pyrogram.Client', owned_gift_id: 'str', price: 'types.GiftResalePrice | None' = None) -> 'bool'
```

Change resale price of a unique gift owned by the current user.

### set_global_privacy_settings

Доступен через client_call.

```python
set_global_privacy_settings(self: 'pyrogram.Client', archive_and_mute_new_chats: 'bool | None' = None, keep_unmuted_chats_archived: 'bool | None' = None, keep_chats_from_folders_archived: 'bool | None' = None, show_read_date: 'bool | None' = None, allow_new_chats_from_unknown_users: 'bool | None' = None, incoming_paid_message_star_count: 'int | None' = None, show_gift_button: 'bool | None' = None, accepted_gift_types: 'types.AcceptedGiftTypes | None' = None) -> 'types.GlobalPrivacySettings'
```

Set account global privacy settings.

### set_inactive_session_ttl

Доступен через client_call.

```python
set_inactive_session_ttl(self: 'pyrogram.Client', inactive_session_ttl_days: 'int') -> 'bool'
```

Changes the period of inactivity after which sessions will automatically be terminated.

### set_main_profile_tab

Доступен через client_call.

```python
set_main_profile_tab(self: 'pyrogram.Client', chat_id: 'int | str', main_profile_tab: 'enums.ProfileTab') -> 'bool'
```

Changes the main profile tab of the user or channel.

### set_managed_bot_access_settings

Доступен через client_call.

```python
set_managed_bot_access_settings(self: 'pyrogram.Client', user_id: 'int | str', is_access_restricted: 'bool', added_user_ids: 'list[int | str] | None' = None) -> 'bool'
```

Use this method to get the access settings of a managed bot.

### set_parse_mode

Синхронный метод: не доступен через асинхронный client_call.

```python
set_parse_mode(self, parse_mode: 'enums.ParseMode | None')
```

Set the parse mode to be used globally by the client.

### set_personal_channel

Доступен через client_call.

```python
set_personal_channel(self: 'pyrogram.Client', chat_id: 'int | str | None' = None) -> 'bool'
```

Set a personal channel in bio.

### set_pinned_gifts

Доступен через client_call.

```python
set_pinned_gifts(self: 'pyrogram.Client', owner_id: 'int | str', owned_gift_ids: 'list[str]') -> 'bool'
```

Change the list of pinned gifts on the current user.

### set_privacy

Доступен через client_call.

```python
set_privacy(self: 'pyrogram.Client', key: 'enums.PrivacyKey', rules: 'list[types.InputPrivacyRuleAllowAll | types.InputPrivacyRuleAllowBots | types.InputPrivacyRuleAllowChats | types.InputPrivacyRuleAllowCloseFriends | types.InputPrivacyRuleAllowContacts | types.InputPrivacyRuleAllowPremium | types.InputPrivacyRuleAllowUsers | types.InputPrivacyRuleDisallowAll | types.InputPrivacyRuleDisallowBots | types.InputPrivacyRuleDisallowChats | types.InputPrivacyRuleDisallowContacts | types.InputPrivacyRuleDisallowUsers]') -> 'list[types.PrivacyRule]'
```

Set account privacy rules.

### set_profile_audio_position

Доступен через client_call.

```python
set_profile_audio_position(self: 'pyrogram.Client', file_id: 'str', after_file_id: 'str | None' = None) -> 'bool'
```

Changes position of an audio file in the profile audio files of the current user.

### set_profile_photo

Доступен через client_call.

```python
set_profile_photo(self: 'pyrogram.Client', photo: 'types.InputChatPhoto | None' = None, is_public: 'bool | None' = None, *, video: 'PathType | BinaryIO | None' = None) -> 'bool'
```

Changes a profile photo for the current user.

### set_send_as_chat

Доступен через client_call.

```python
set_send_as_chat(self: 'pyrogram.Client', chat_id: 'int | str', send_as_chat_id: 'int | str') -> 'bool'
```

Set the default "send_as" chat for a chat.

### set_slow_mode

Доступен через client_call.

```python
set_slow_mode(self: 'pyrogram.Client', chat_id: 'int | str', seconds: 'int | None') -> 'bool'
```

Set the slow mode interval for a chat.

### set_upgraded_gift_colors

Доступен через client_call.

```python
set_upgraded_gift_colors(self: 'pyrogram.Client', upgraded_gift_colors_id: 'int') -> 'bool'
```

Changes color scheme for the current user based on an owned or a hosted upgraded gift.

### set_username

Доступен через client_call.

```python
set_username(self: 'pyrogram.Client', username: 'str | None') -> 'bool'
```

Set your own username.

### show_chat_stories

Доступен через client_call.

```python
show_chat_stories(self: 'pyrogram.Client', chat_id: 'int | str') -> 'bool'
```

Show the active stories of a user and display them in the action bar on the homescreen.

### show_gift

Доступен через client_call.

```python
show_gift(self: 'pyrogram.Client', owned_gift_id: 'str') -> 'bool'
```

Display gift on the current user's or the channel's profile page.

### sign_in

Недоступен через client_call: исключён политикой моста.

```python
sign_in(self: 'pyrogram.Client', phone_number: 'str', phone_code_hash: 'str', phone_code: 'str') -> 'types.User | types.TermsOfService | bool'
```

Authorize a user in Telegram with a valid confirmation code.

### sign_in_bot

Доступен через client_call.

```python
sign_in_bot(self: 'pyrogram.Client', bot_token: 'str') -> 'types.User'
```

Authorize a bot using its bot token generated by BotFather.

### sign_up

Недоступен через client_call: исключён политикой моста.

```python
sign_up(self: 'pyrogram.Client', phone_number: 'str', phone_code_hash: 'str', first_name: 'str', last_name: 'str' = '') -> 'types.User'
```

Register a new user in Telegram.

### start

Недоступен через client_call: исключён политикой моста.

```python
start(self: 'pyrogram.Client', *, use_qr: 'bool' = False, except_ids: 'list[int] | None' = None) -> 'pyrogram.Client'
```

Start the client.

### start_bot

Доступен через client_call.

```python
start_bot(self: 'pyrogram.Client', chat_id: 'int | str', param: 'str' = '') -> 'types.Message | None'
```

Start bot

### stop

Недоступен через client_call: исключён политикой моста.

```python
stop(self: 'pyrogram.Client', block: 'bool' = True, clear_handlers: 'bool' = True) -> 'pyrogram.Client'
```

Stop the Client.

### stop_poll

Доступен через client_call.

```python
stop_poll(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', reply_markup: 'types.InlineKeyboardMarkup | None' = None) -> 'types.Poll'
```

Stop a poll which was sent by you.

### stop_transmission

Синхронный метод: не доступен через асинхронный client_call.

```python
stop_transmission(self)
```

Stop downloading or uploading a file.

### stream_media

Доступен через client_call.

```python
stream_media(self: 'pyrogram.Client', message: 'types.Message | str', limit: 'int' = 0, offset: 'int' = 0) -> 'AsyncGenerator[bytes, None]'
```

Stream the media from a message chunk by chunk.

### suggest_birthday

Доступен через client_call.

```python
suggest_birthday(self: 'pyrogram.Client', chat_id: 'int | str', birthday: 'types.Birthday') -> 'bool'
```

Suggests a birthdate to another regular user with common messages and allowing non-paid messages.

### summarize_message

Доступен через client_call.

```python
summarize_message(self: 'pyrogram.Client', chat_id: 'str', message_id: 'int', translate_to_language_code: 'str | None' = None, tone: 'str | None' = None) -> 'types.FormattedText'
```

Summarizes content of the message with non-empty summary_language_code.

### terminate

Недоступен через client_call: исключён политикой моста.

```python
terminate(self: 'pyrogram.Client', clear_handlers: 'bool' = True)
```

Terminate the client by shutting down workers.

### toggle_folder_tags

Доступен через client_call.

```python
toggle_folder_tags(self: 'pyrogram.Client', are_tags_enabled: 'bool') -> 'bool'
```

Toggles whether chat folder tags are enabled.

### toggle_forum_topics

Доступен через client_call.

```python
toggle_forum_topics(self: 'pyrogram.Client', chat_id: 'int | str', is_forum: 'bool' = False, has_forum_tabs: 'bool' = False) -> 'bool'
```

Enable or disable forum functionality in a supergroup.

### toggle_join_to_send

Доступен через client_call.

```python
toggle_join_to_send(self: 'pyrogram.Client', chat_id: 'int | str', enabled: 'bool' = False) -> 'bool'
```

Enable or disable guest users' ability to send messages in a supergroup.

### transfer_business_account_stars

Доступен через client_call.

```python
transfer_business_account_stars(self: 'pyrogram.Client', business_connection_id: 'str', star_count: 'int') -> 'bool'
```

Transfers Telegram Stars from the business account balance to the bot’s balance.

### transfer_chat_ownership

Доступен через client_call.

```python
transfer_chat_ownership(self: 'pyrogram.Client', chat_id: 'int | str', user_id: 'int | str', password: 'str') -> 'bool'
```

Change the owner of a chat or channel.

### transfer_gift

Доступен через client_call.

```python
transfer_gift(self: 'pyrogram.Client', owned_gift_id: 'str', new_owner_chat_id: 'int | str', business_connection_id: 'str | None' = None) -> 'types.Message | None'
```

Transfers an owned unique gift to another user.

### translate_message_text

Доступен через client_call.

```python
translate_message_text(self: 'pyrogram.Client', chat_id: 'str', message_id: 'int', to_language_code: 'str | None' = None, tone: 'str | None' = None) -> 'types.FormattedText'
```

Extract text or caption of the given message and translates it to the given language.

### translate_text

Доступен через client_call.

```python
translate_text(self: 'pyrogram.Client', text: 'str | types.FormattedText', to_language_code: 'str | None' = None, tone: 'str | None' = None) -> 'types.FormattedText'
```

Translate a text to the given language.

### unarchive_chats

Доступен через client_call.

```python
unarchive_chats(self: 'pyrogram.Client', chat_ids: 'int | str | list[int | str]') -> 'bool'
```

Unarchive one or more chats.

### unban_chat_member

Доступен через client_call.

```python
unban_chat_member(self: 'pyrogram.Client', chat_id: 'int | str', user_id: 'int | str') -> 'bool'
```

Unban a previously banned user in a supergroup or channel.
The user will **not** return to the group or channel automatically, but will be able to join via link, etc.
You must be an administrator for this to work.

### unblock_user

Доступен через client_call.

```python
unblock_user(self: 'pyrogram.Client', user_id: 'int | str') -> 'bool'
```

Unblock a user.

### unpin_all_chat_messages

Доступен через client_call.

```python
unpin_all_chat_messages(self: 'pyrogram.Client', chat_id: 'int | str') -> 'bool'
```

Use this method to clear the list of pinned messages in a chat.
If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have
the 'can_pin_messages' admin right in a super

### unpin_chat_message

Доступен через client_call.

```python
unpin_chat_message(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int' = 0, business_connection_id: 'str | None' = None) -> 'bool'
```

Unpin a message in a group, channel or your own chat.
You must be an administrator in the chat for this to work and must have the "can_pin_messages" admin
right in the supergroup or "can_edit_messages" admin right in the

### unpin_chat_stories

Доступен через client_call.

```python
unpin_chat_stories(self: 'pyrogram.Client', chat_id: 'int | str', stories_ids: 'int | Iterable[int]') -> 'list[int]'
```

Unpin one or more stories in a chat by using stories identifiers.

### unpin_forum_topic

Доступен через client_call.

```python
unpin_forum_topic(self: 'pyrogram.Client', chat_id: 'int | str', topic_id: 'int') -> 'bool'
```

Unpin a forum topic.

### update_birthday

Доступен через client_call.

```python
update_birthday(self: 'pyrogram.Client', day: 'int | None' = None, month: 'int | None' = None, year: 'int | None' = None) -> 'bool'
```

Update birthday in your profile.

### update_chat_notifications

Доступен через client_call.

```python
update_chat_notifications(self: 'pyrogram.Client', chat_id: 'int | str', mute: 'bool | None' = None, mute_until: 'datetime | None' = None, stories_muted: 'bool | None' = None, stories_hide_sender: 'bool | None' = None, show_previews: 'bool | None' = None) -> 'bool'
```

Update the notification settings for the selected chat

### update_profile

Доступен через client_call.

```python
update_profile(self: 'pyrogram.Client', first_name: 'str | None' = None, last_name: 'str | None' = None, bio: 'str | None' = None) -> 'bool'
```

Update your profile details such as first name, last name and bio.

### update_status

Доступен через client_call.

```python
update_status(self: 'pyrogram.Client', offline: 'bool' = False) -> 'bool'
```

Update your profile status.

### updates_watchdog

Доступен через client_call.

```python
updates_watchdog(self)
```



### upgrade_gift

Доступен через client_call.

```python
upgrade_gift(self: 'pyrogram.Client', owned_gift_id: 'str', keep_original_details: 'bool | None' = None, star_count: 'int | None' = None, business_connection_id: 'str | None' = None) -> 'types.Message | None'
```

Upgrade a given regular gift to a unique gift.

### view_messages

Доступен через client_call.

```python
view_messages(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int | list[int]') -> 'bool'
```

Increment message views counter.

### view_stories

Доступен через client_call.

```python
view_stories(self: 'pyrogram.Client', chat_id: 'int | str', story_id: 'int | list[int]') -> 'bool'
```

Increment story views.

### vote_poll

Доступен через client_call.

```python
vote_poll(self: 'pyrogram.Client', chat_id: 'int | str', message_id: 'int', options: 'int | list[int]') -> 'types.Poll'
```

Vote a poll.
